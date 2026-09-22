import rclpy

from rclpy.node import Node
from my_interfaces.msg import RobotCommand


class RobotCommandPublisher(Node):

    def __init__(self):
        super().__init__('robot_command_publisher')

        self.publisher = self.create_publisher(
            RobotCommand,
            'robot_command',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_command
        )

    def publish_command(self):

        msg = RobotCommand()

        msg.robot_name = 'robot1'

        msg.target_pose.position.x = 1.0
        msg.target_pose.position.y = 2.0
        msg.target_pose.position.z = 0.5

        msg.target_pose.orientation.x = 0.0
        msg.target_pose.orientation.y = 0.0
        msg.target_pose.orientation.z = 0.0
        msg.target_pose.orientation.w = 1.0

        msg.speed = 0.5
        msg.enable = True

        msg.joint_angles = [
            0.0,
            30.0,
            -20.0,
            90.0,
            0.0,
            10.0
        ]

        msg.mode = RobotCommand.MODE_MOVING

        self.publisher.publish(msg)

        self.get_logger().info(
            f'Robot: {msg.robot_name}, '
            f'Position: '
            f'({msg.target_pose.position.x}, '
            f'{msg.target_pose.position.y}, '
            f'{msg.target_pose.position.z}), '
            f'Speed: {msg.speed}, '
            f'Mode: {msg.mode}'
        )


def main(args=None):

    rclpy.init(args=args)

    node = RobotCommandPublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()