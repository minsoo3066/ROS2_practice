import os
from glob import glob

from setuptools import find_packages, setup

package_name = 'my_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'publisher = my_pubsub.publisher:main',
            'subscriber = my_pubsub.subscriber:main',
            'service_server = my_pubsub.service_server:main',
            'service_client = my_pubsub.service_client:main',
            'action_server = my_pubsub.action_server:main',
            'action_client = my_pubsub.action_client:main',
        ],
    },
)
