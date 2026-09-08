import time
import rclpy

from rclpy.node import Node
from rclpy.action import ActionServer, GoalResponse
from example_interfaces.action import Fibonacci

class FibonacciActionServer(Node):

    def __init__(self):

        super().__init__('action_server')

        self.action_server = ActionServer(
            self, # 속해 있는 Node
            Fibonacci, # Action 타입
            'fibonacci', # Action 이름
            self.execute_callback, # Goal 실행 담당 함수
            goal_callback=self.goal_callback # 새로운 Goal 요청이 들어올시 실행할 함수
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

    def goal_callback(self, goal_request): # ServerGoalHandle이 아닌 Goal 요청 객체가 들어옴
        # Goal을 받을지 말지 결정하기 전이기 때문에 Handle이 아님
        # ServerGoalHandle은 Accepted 이후 의미를 가짐

        self.get_logger().info(
            f'Received Goal: order = {goal_request.order}'
        )

        if goal_request.order < 2:
            self.get_logger().info('Goal rejected')

            return GoalResponse.REJECT

        self.get_logger().info('Goal accepted')

        return GoalResponse.ACCEPT


def main(args=None):

    rclpy.init(args=args)

    node = FibonacciActionServer()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()