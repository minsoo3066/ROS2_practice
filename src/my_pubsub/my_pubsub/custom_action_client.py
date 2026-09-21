import rclpy

from rclpy.node import Node
from rclpy.action import ActionClient

from my_interfaces.action import MoveRobot


class CustomActionClient(Node):

    def __init__(self):
        super().__init__('custom_action_client')

        self.action_client = ActionClient(
            self,
            MoveRobot,
            'move_robot'
        )

    def send_goal(self):

        goal_msg = MoveRobot.Goal()

        goal_msg.x = 3.0
        goal_msg.y = 4.0

        self.action_client.wait_for_server()

        self.send_goal_future = (
            self.action_client.send_goal_async(
                goal_msg,
                feedback_callback=self.feedback_callback
            )
        )

        self.send_goal_future.add_done_callback(
            self.goal_response_callback
        )

    def goal_response_callback(self, future):

        goal_handle = future.result()

        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            return

        self.get_logger().info('Goal accepted')

        self.get_result_future = (
            goal_handle.get_result_async()
        )

        self.get_result_future.add_done_callback(
            self.result_callback
        )

    def feedback_callback(self, feedback_msg):

        feedback = feedback_msg.feedback

        self.get_logger().info(
            f'Progress: {feedback.progress}%'
        )

    def result_callback(self, future):

        result = future.result().result

        self.get_logger().info(
            f'Success: {result.success}'
        )

        self.get_logger().info(
            f'Message: {result.message}'
        )

        rclpy.shutdown()


def main(args=None):

    rclpy.init(args=args)

    node = CustomActionClient()

    node.send_goal()

    rclpy.spin(node)


if __name__ == '__main__':
    main()