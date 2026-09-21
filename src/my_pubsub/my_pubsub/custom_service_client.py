import rclpy

from rclpy.node import Node
from my_interfaces.srv import SetTarget


class CustomServiceClient(Node):

    def __init__(self):
        super().__init__('custom_service_client')

        self.client = self.create_client(
            SetTarget,
            'set_target'
        )

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(
                'Waiting for SetTarget service...'
            )

        request = SetTarget.Request()

        request.x = 1.5
        request.y = 2.0

        self.future = self.client.call_async(request)


def main(args=None):

    rclpy.init(args=args)

    node = CustomServiceClient()

    rclpy.spin_until_future_complete(
        node,
        node.future
    )

    response = node.future.result()

    node.get_logger().info(
        f'Success: {response.success}'
    )

    node.get_logger().info(
        f'Message: {response.message}'
    )

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()