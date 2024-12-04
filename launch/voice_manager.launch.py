from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    package_name = 'voice_manager'

    config_file = os.path.join(
        get_package_share_directory(package_name),
        'config',
        'config_voice_manager.yaml'
    )

    voice_manager_node = Node(
        package=package_name,
        executable='voice_manager',
        name='voice_manager_node',
        output='screen',
        parameters=[config_file]
    )

    raspicat_speak2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('raspicat_speak2'),
                'launch',
                'raspicat_speak2.launch.py'
            )
        )
    )

    return LaunchDescription([
        voice_manager_node,
        raspicat_speak2_launch,
    ])
