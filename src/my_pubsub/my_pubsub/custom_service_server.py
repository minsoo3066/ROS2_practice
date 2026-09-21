import rclpy

from rclpy.node import Node
from my_interfaces.srv import SetTarget


class CustomServiceServer(Node):

    def __init__(self):
        super().__init__('custom_service_server')

        self.service = self.create_service(
            SetTarget,
            'set_target',
            self.set_target_callback
        )

        self.get_logger().info('SetTarget service ready')

    def set_target_callback(self, request, response):

        self.get_logger().info(
            f'Received target: x={request.x}, y={request.y}'
        )

        response.success = True
        response.message = (
            f'Target accepted: x={request.x}, y={request.y}'
        )

        return response


def main(args=None):

    rclpy.init(args=args)

    node = CustomServiceServer()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()