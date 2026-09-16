from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    robot1_publisher = Node(
        package='my_pubsub',
        executable='publisher',
        name='launch_publisher',
        namespace='robot1',
        output='screen',
        parameters=[
            {
                'timer_period': 1.0
            }
        ],
        remappings=[
            ('chatter', 'robot_message')
        ]
    )

    robot1_subscriber = Node(
        package='my_pubsub',
        executable='subscriber',
        name='launch_subscriber',
        namespace='robot1',
        output='screen',
        remappings=[
            ('chatter', 'robot_message')
        ]
    )

    robot2_publisher = Node(
        package='my_pubsub',
        executable='publisher',
        name='launch_publisher',
        namespace='robot2',
        output='screen',
        parameters=[
            {
                'timer_period': 2.0
            }
        ],
        remappings=[
            ('chatter', 'robot_message')
        ]
    )

    robot2_subscriber = Node(
        package='my_pubsub',
        executable='subscriber',
        name='launch_subscriber',
        namespace='robot2',
        output='screen',
        remappings=[
            ('chatter', 'robot_message')
        ]
    )

    return LaunchDescription([
        robot1_publisher,
        robot1_subscriber,
        robot2_publisher,
        robot2_subscriber
    ])
