import rclpy

from rclpy.node import Node

from tf2_ros import Buffer
from tf2_ros import TransformListener
from tf2_ros import TransformException


class TFListener(Node):

    def __init__(self):
        super().__init__('tf_listener')

        self.tf_buffer = Buffer()

        self.tf_listener = TransformListener(
            self.tf_buffer,
            self
        )

        self.timer = self.create_timer(
            1.0,
            self.lookup_transform
        )

    def lookup_transform(self):

        try:

            transform = self.tf_buffer.lookup_transform(
                'world',
                'camera',
                rclpy.time.Time()
            )

        except TransformException as ex:

            self.get_logger().info(
                f'Could not transform: {ex}'
            )

            return

        self.get_logger().info(
            f'Camera position: '
            f'x={transform.transform.translation.x:.2f}, '
            f'y={transform.transform.translation.y:.2f}, '
            f'z={transform.transform.translation.z:.2f}'
        )


def main(args=None):

    rclpy.init(args=args)

    node = TFListener()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()