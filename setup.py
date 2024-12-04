from setuptools import find_packages, setup

package_name = 'voice_manager'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/config', ['config/config_voice_manager.yaml']),
        ('share/' + package_name + '/launch', ['launch/voice_manager.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kazuma',
    maintainer_email='kazulab10969@outlook.jp',
    description='Voice manager package for ROS 2',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'voice_manager = voice_manager.voice_manager:main'
        ],
    },
)
