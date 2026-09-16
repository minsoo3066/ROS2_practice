import rclpy # Node 생성 및 설정을 위한 라이브러리

from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy
from std_msgs.msg import String

class Publisher(Node): # Node 상속

    def __init__(self): 
        super().__init__("my_publisher") # 이름 설정

        qos_profile = QoSProfile(
            depth=10,
            reliability=ReliabilityPolicy.RELIABLE,
            durability=DurabilityPolicy.VOLATILE
        )

        self.publisher = self.create_publisher(
            String, # 메시지 종류
            "chatter", # Topic 종류
            qos_profile # QoS 설정
        )

        self.declare_parameter('timer_period', 1.0) # 타이머 설정값 등록
        
        timer_period = self.get_parameter('timer_period').value # 설정값 읽기

        self.timer = self.create_timer(
            timer_period, # timer_period sec 주기로
            self.publish_message # publish_message 실행
        )

        self.count = 0


    def publish_message(self):

        msg = String() # String 메시지 제작

        msg.data = f"Hello ROS2! cont = {self.count}" # 데이터 삽입

        self.publisher.publish(msg) # 토픽 발행 

        self.get_logger().info(
            f"Publishing: {msg.data}"
        )

        self.count += 1



def main(args=None):

    rclpy.init(args=args) # ros2 초기화

    node = Publisher() # 노드 생성

    rclpy.spin(node) # 노드를 계속 실행시키며 ros2 이벤트 처리

    node.destroy_node() # 노드 종료
    rclpy.shutdown() # ros2 종료



if __name__ == "__main__":
    main()