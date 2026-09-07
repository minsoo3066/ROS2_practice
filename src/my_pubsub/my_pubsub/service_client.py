import rclpy

from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class ServiceClient(Node):

    def __init__(self):
        super().__init__('service_client')

        self.client = self.create_client(
            AddTwoInts,
            'add_two_ints'
        )

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting...')


    def send_request(self, a, b):

        request = AddTwoInts.Request()

        request.a = a
        request.b = b

        future = self.client.call_async(request)

        return future


def main(args=None):

    rclpy.init(args=args)

    node = ServiceClient()

    future = node.send_request(10, 20)

    rclpy.spin_until_future_complete(node, future)

    response = future.result()

    node.get_logger().info(
        f'Result: {response.sum}'
    )

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
