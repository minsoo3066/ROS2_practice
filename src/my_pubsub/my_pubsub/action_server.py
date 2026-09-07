import time
import rclpy

from rclpy.node import Node
from rclpy.action import ActionServer
from example_interfaces.action import Fibonacci

class FibonacciActionServer(Node):

    def __init__(self):

        super().__init__('action_server')

        self.action_server = ActionServer(
            self, # 속해 있는 Node
            Fibonacci, # Action 타입
            'fibonacci', # Action 이름
            self.execute_callback # Goal 실행 담당 함수
        )

        self.get_logger().info('Action Server Ready')

    def execute_callback(self, goal_handle):

        self.get_logger().info(
            f'Executing Goal: order = {goal_handle.request.order}'
        )

        # 피드백 메시지 생성
        feedback = Fibonacci.Feedback()

        feedback.sequence = [0, 1]


        # 피보나치 계산
        for i in range(1, goal_handle.request.order):

            feedback.sequence.append(
                feedback.sequence[i] + feedback.sequence[i-1]
            )

            self.get_logger().info(
                f'Feedback: {feedback.sequence}'
            )

            # 클라이언트에게 중간 진행 상황 전달
            goal_handle.publish_feedback(feedback)

            time.sleep(1.0)


        # Goal이 성공적으로 완료 되었음을 표시
        goal_handle.succeed()

        # Result 생성
        result = Fibonacci.Result()

        result.sequence = feedback.sequence

        return result


def main(args=None):

    rclpy.init(args=args)

    node = FibonacciActionServer()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()