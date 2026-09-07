import time

import rclpy

from rclpy.node import Node
from rclpy.action import ActionServer
from example_interfaces.action import Fibonacci


class FibonacciActionServer(Node):

    def __init__(self):
        super().__init__('action_server')

        self.action_server = ActionServer(
            self,
            Fibonacci,
            'fibonacci',
            self.execute_callback
        )

        self.get_logger().info('Action Server Ready')


    def execute_callback(self, goal_handle):

        self.get_logger().info(
            f'Executing Goal: order = {goal_handle.request.order}'
        )

        feedback = Fibonacci.Feedback()
        feedback.sequence = [0, 1]

        for i in range(1, goal_handle.request.order):

            feedback.sequence.append(
                feedback.sequence[i] + feedback.sequence[i - 1]
            )

            self.get_logger().info(
                f'Feedback: {feedback.sequence}'
            )

            goal_handle.publish_feedback(feedback)

            time.sleep(1.0)

        goal_handle.succeed()

        result = Fibonacci.Result()
        result.sequence = feedback.sequence

        return result


def main(args=None):

    rclpy.init(args=args)

    node = FibonacciActionServer()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
