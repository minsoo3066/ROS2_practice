import threading
import time

import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import ReentrantCallbackGroup


class ExecutorTest(Node):

    def __init__(self):
        super().__init__('executor_test')

        self.fast_timer = self.create_timer(
            0.5,
            self.fast_callback
        )

        self.slow_timer = self.create_timer(
            2.0,
            self.slow_callback
        )

        self.callback_group = ReentrantCallbackGroup()

        self.timer_a = self.create_timer(
            2.0,
            self.callback_a,
            callback_group=self.callback_group
        )

        self.timer_b = self.create_timer(
            2.0,
            self.callback_b,
            callback_group=self.callback_group
        )

        self.timer_c = self.create_timer(
            2.0,
            self.callback_c,
            callback_group=self.callback_group
        )

    def fast_callback(self):
        self.get_logger().info('FAST callback')

    def slow_callback(self):
        self.get_logger().info('SLOW callback START')

        time.sleep(3.0)

        self.get_logger().info('SLOW callback END')

    def callback_a(self):
        self.get_logger().info(
            f'A START - thread: {threading.get_ident()}'
        )

        time.sleep(3.0)

        self.get_logger().info('A END')


    def callback_b(self):
        self.get_logger().info(
            f'B START - thread: {threading.get_ident()}'
        )

        time.sleep(3.0)

        self.get_logger().info('B END')


    def callback_c(self):
        self.get_logger().info(
            f'C START - thread: {threading.get_ident()}'
        )

        time.sleep(3.0)

        self.get_logger().info('C END')


def main(args=None):

    rclpy.init(args=args)

    node = ExecutorTest()

    executor = MultiThreadedExecutor()

    executor.add_node(node)

    executor.spin()

    executor.shutdown()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()