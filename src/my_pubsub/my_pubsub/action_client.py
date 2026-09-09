import rclpy

from rclpy.node import Node
from rclpy.action import ActionClient
from action_msgs.msg import GoalStatus
from example_interfaces.action import Fibonacci

class FibonacciActionClient(Node):

    def __init__(self):
        super().__init__('action_client')

        self.done = False
        self.cancel_sent = False
        self.goal_handle = None

        self.action_client = ActionClient(
            self, # 어느 노드에 속해있는가
            Fibonacci, # 인터페이스 타입
            'fibonacci' # 이름
        )

    def send_goal(self, order):

        goal_msg = Fibonacci.Goal()
        goal_msg.order = order

        self.action_client.wait_for_server()

        self.send_goal_future = self.action_client.send_goal_async( 
            # Server가 Goal을 Accepted 했는가
            goal_msg,
            feedback_callback = self.feedback_callback # feedback올 시 실행
            )
        # goal 응답 도착 시 future 반환
        # 그동안 feedback 도착 시 실행할 함수 지정

        self.send_goal_future.add_done_callback( # future가 완료되면 실행할 callback
            self.goal_response_callback
        )

    def goal_response_callback(self, future):

        self.goal_handle = future.result() 
        # 완료 되었을 때 실행되는 callback 함수 안이므로 바로 result를 꺼낼 수 있음
        # 최종 result가 아닌 ClientGoalHandle (goal accept/ reject)


        if not self.goal_handle.accepted: # future가 accepted 안되는지 체크
            self.get_logger().info('Goal rejected')
            self.done = True
            return

        self.get_logger().info('Goal accepted')

        self.get_result_future = self.goal_handle.get_result_async()  # Accepted 한 Goal의 작업이 끝났는가
        # 해당 goal의 결과를 비동기로 기다리겠다, future 반환

        self.get_result_future.add_done_callback( # 작업 완료 들어오면 실행
            self.get_result_callback
        )

    def get_result_callback(self, future): # Action의 최종결과 응답을 기다리던 Future

        response = future.result()
        # future.result() -> Future 안에 들어온 결과 객체 즉, response 응답의 결과
        # response 에는 status, result 속성 두 개가 들어 있음
        # status 는 succeeded, aborted, canceled 여부
        # result 안에는 sequence

        result = response.result
        # 해당 result가 Action의 result

        if response.status == GoalStatus.STATUS_SUCCEEDED:

            self.get_logger().info(
                f'Goal succeeded: {result.sequence}'
            )

        elif response.status == GoalStatus.STATUS_CANCELED:

            self.get_logger().info(
                f'Goal canceled: {result.sequence}'
            )

        elif response.status == GoalStatus.STATUS_ABORTED:

            self.get_logger().info(
                f'Goal aborted: {result.sequence}'
            )

        else:

            self.get_logger().info(
                f'Goal finished with status: {response.status}'
            )

        self.done = True # 생명주기 END 
        

    def feedback_callback(self, feedback_msg):

        feedback = feedback_msg.feedback

        self.get_logger().info(
            f'Feedback: {feedback.sequence}'
        )

        if len(feedback.sequence) >= 5 and not self.cancel_sent and self.goal_handle is not None:

            self.cancel_sent = True

            self.cancel_goal()


    def cancel_goal(self):

        self.get_logger().info('Sending cancel request')

        self.cancel_future = self.goal_handle.cancel_goal_async()

        self.cancel_future.add_done_callback(
            self.cancel_response_callback
        )

    def cancel_response_callback(self, future):

        response = future.result()

        if len(response.goals_canceling) > 0:
            self.get_logger().info('Cancel accepted')
        else:
            self.get_logger().info('Cancel rejected')

def main(args=None):

    rclpy.init(args=args) # 초기화

    node = FibonacciActionClient() # 노드 객체 생성

    node.send_goal(10)

    while rclpy.ok() and not node.done:
        rclpy.spin_once(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
