import rclpy

from rclpy.node import Node
from my_interfaces.msg import RobotCommand


class RobotCommandSubscriber(Node):

    def __init__(self):
        super().__init__('robot_command_subscriber')

        self.subscription = self.create_subscription(
            RobotCommand,
            'robot_command',
            self.command_callback,
            10
        )

    def command_callback(self, msg):

        self.get_logger().info(
            f'Robot: {msg.robot_name}'
        )

        self.get_logger().info(
            f'Position: '
            f'x={msg.target_pose.position.x}, '
            f'y={msg.target_pose.position.y}, '
            f'z={msg.target_pose.position.z}'
        )

        self.get_logger().info(
            f'Orientation: '
            f'x={msg.target_pose.orientation.x}, '
            f'y={msg.target_pose.orientation.y}, '
            f'z={msg.target_pose.orientation.z}, '
            f'w={msg.target_pose.orientation.w}'
        )

        self.get_logger().info(
            f'Speed: {msg.speed}'
        )

        self.get_logger().info(
            f'Enable: {msg.enable}'
        )

        self.get_logger().info(
            f'Joint angles: {msg.joint_angles}'
        )

        if msg.mode == RobotCommand.MODE_IDLE:
            mode_name = 'IDLE'

        elif msg.mode == RobotCommand.MODE_MOVING:
            mode_name = 'MOVING'

        elif msg.mode == RobotCommand.MODE_ERROR:
            mode_name = 'ERROR'

        else:
            mode_name = 'UNKNOWN'

        self.get_logger().info(
            f'Mode: {mode_name}'
        )


def main(args=None):

    rclpy.init(args=args)

    node = RobotCommandSubscriber()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()