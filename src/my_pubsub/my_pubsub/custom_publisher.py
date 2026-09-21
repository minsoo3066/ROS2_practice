import rclpy

from rclpy.node import Node
from my_interfaces.msg import RobotStatus


class CustomPublisher(Node):

    def __init__(self):
        super().__init__('custom_publisher')

        self.publisher = self.create_publisher(
            RobotStatus,
            'robot_status',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_status
        )

        self.battery = 100

    def publish_status(self):

        msg = RobotStatus()

        msg.robot_name = 'robot1'
        msg.battery = self.battery
        msg.is_moving = True

        self.publisher.publish(msg)

        self.get_logger().info(
            f'Robot: {msg.robot_name}, '
            f'Battery: {msg.battery}, '
            f'Moving: {msg.is_moving}'
        )

        self.battery -= 1


def main(args=None):

    rclpy.init(args=args)

    node = CustomPublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()