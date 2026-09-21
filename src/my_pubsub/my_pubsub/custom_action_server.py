import time

import rclpy

from rclpy.node import Node
from rclpy.action import ActionServer

from my_interfaces.action import MoveRobot


class CustomActionServer(Node):

    def __init__(self):
        super().__init__('custom_action_server')

        self.action_server = ActionServer(
            self,
            MoveRobot,
            'move_robot',
            self.execute_callback
        )

        self.get_logger().info('MoveRobot Action Server ready')

    def execute_callback(self, goal_handle):

        target_x = goal_handle.request.x
        target_y = goal_handle.request.y

        self.get_logger().info(
            f'Moving to x={target_x}, y={target_y}'
        )

        feedback = MoveRobot.Feedback()

        for i in range(1, 6):

            feedback.progress = i * 20.0

            goal_handle.publish_feedback(feedback)

            self.get_logger().info(
                f'Progress: {feedback.progress}%'
            )

            time.sleep(1.0)

        goal_handle.succeed()

        result = MoveRobot.Result()

        result.success = True
        result.message = (
            f'Target reached: x={target_x}, y={target_y}'
        )

        return result


def main(args=None):

    rclpy.init(args=args)

    node = CustomActionServer()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()