import rclpy

from rclpy.node import Node
from my_interfaces.msg import RobotStatus


class CustomSubscriber(Node):

    def __init__(self):
        super().__init__('custom_subscriber')

        self.subscription = self.create_subscription(
            RobotStatus,
            'robot_status',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):

        self.get_logger().info(
            f'Robot: {msg.robot_name}, '
            f'Battery: {msg.battery}, '
            f'Moving: {msg.is_moving}'
        )


def main(args=None):

    rclpy.init(args=args)

    node = CustomSubscriber()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()