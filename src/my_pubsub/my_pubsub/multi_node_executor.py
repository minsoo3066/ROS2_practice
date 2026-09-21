import rclpy

from rclpy.executors import MultiThreadedExecutor

from my_pubsub.publisher import Publisher
from my_pubsub.subscriber import Subscriber


def main(args=None):

    rclpy.init(args=args)

    publisher_node = Publisher()
    subscriber_node = Subscriber()

    executor = MultiThreadedExecutor(num_threads=2)

    executor.add_node(publisher_node)
    executor.add_node(subscriber_node)

    executor.spin()

    executor.shutdown()

    publisher_node.destroy_node()
    subscriber_node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()