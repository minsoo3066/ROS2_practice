import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class ServiceClient(Node):

    def __init__(self):
        super().__init__('service_client')

        self.client = self.create_client(
            AddTwoInts, #서비스 타입
            'add_two_ints' # 서비스 명
        )

        while not self.client.wait_for_service(timeout_sec=1.0): # 서비스가 준비되어있지 않다면
            self.get_logger().info('Service not available, waiting...') # log 띄워라


    def send_request(self, a, b):

        request = AddTwoInts.Request() # request 생성

        request.a = a
        request.b = b

        future = self.client.call_async(request) # call -> 서비스호출, async -> 비동기 (응답을 기다리는 동안에도 작동)

        return future # 미래에 결과가 들어올 객체


def main(args=None):

    rclpy.init(args=args)

    node = ServiceClient()

    future = node.send_request(10, 20)

    rclpy.spin_until_future_complete(node, future) # ros2 이벤트를 처리하면 future에 결과가 들어올 때까지 기다려라

    response = future.result()

    node.get_logger().info(
        f'Result: {response.sum}'
    )

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()