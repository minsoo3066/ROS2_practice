import math

import rclpy

from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster


class DynamicTFBroadcaster(Node):

    def __init__(self):
        super().__init__('dynamic_tf_broadcaster')

        self.tf_broadcaster = TransformBroadcaster(self)

        self.x = 0.0
        self.yaw = 0.0

        self.timer = self.create_timer(
            0.1,
            self.broadcast_transform
        )

    def broadcast_transform(self):

        transform = TransformStamped()

        transform.header.stamp = self.get_clock().now().to_msg()

        transform.header.frame_id = 'world'
        transform.child_frame_id = 'base_link'

        # Position
        transform.transform.translation.x = self.x
        transform.transform.translation.y = 0.0
        transform.transform.translation.z = 0.0

        # Yaw -> Quaternion
        transform.transform.rotation.x = 0.0
        transform.transform.rotation.y = 0.0
        transform.transform.rotation.z = math.sin(self.yaw / 2.0)
        transform.transform.rotation.w = math.cos(self.yaw / 2.0)

        self.tf_broadcaster.sendTransform(transform)

        self.get_logger().info(
            f'x={self.x:.2f}, yaw={self.yaw:.2f}'
        )

        self.x += 0.01
        self.yaw += 0.01


def main(args=None):

    rclpy.init(args=args)

    node = DynamicTFBroadcaster()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()