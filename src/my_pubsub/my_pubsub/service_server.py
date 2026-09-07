import rclpy

from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class ServiceServer(Node):

    def __init__(self):
        super().__init__('service_server')

        self.service = self.create_service(
            AddTwoInts, # Service 타입
            'add_two_ints', # Service 이름
            self.add_callback # 요청이 올 시 실행할 callback
        )

        self.get_logger().info('Service Server Ready')


    def add_callback(self, request, response):

        response.sum = request.a + request.b

        self.get_logger().info(
            f'Request: {request.a} + {request.b} = {response.sum}'
        )

        return response


def main(args=None):

    rclpy.init(args=args)

    node = ServiceServer()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
