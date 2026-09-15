from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    publisher_node = Node(
        package='my_pubsub',
        executable='publisher',
        output='screen'
    )

    subscriber_node = Node(
        package='my_pubsub',
        executable='subscriber',
        output='screen'
    )

    return LaunchDescription([
        publisher_node,
        subscriber_node
    ])
