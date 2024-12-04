
# voice_manager

## Overview
The `voice_manager` package is designed for managing text-to-speech interactions in the KUAMS system. It subscribes to an ID and publishes the corresponding text for speech output.

## Features
- Subscribes to `speak_text_id` topic for receiving an ID.
- Publishes corresponding text to `speak` topic for speech synthesis.
- Compatible with the `raspicat_speak2` package for seamless text-to-speech functionality.

## Requirements
- **Operating System**: Ubuntu 22.04
- **ROS2 Distribution**: Humble Hawksbill
- **Dependencies**:
  - [raspicat_speak2](https://github.com/CIT-Autonomous-Robot-Lab/raspicat_speak2)

## Installation
1. Clone the repository into your ROS2 workspace:
   ```bash
   cd ~/your_ros2_workspace/src
   git clone https://github.com/kzm784/voice_manager
   ```
2. Build the workspace:
   ```bash
   cd ~/your_ros2_workspace
   colcon build --packages-select voice_manager
   source install/setup.bash
   ```

## Usage
### Launching the Node
Run the `voice_manager` node using the launch file:
```bash
ros2 launch voice_manager voice_manager_launch.py
```

### Configuration
The package uses a YAML file for configuration. Ensure that the path to your ID-to-text CSV file is correctly specified in `config/config_voice_manager.yaml`:
```yaml
id_to_text_csv: "/path/to/your/id_to_text.csv"
```

### Topics
- **Subscribed Topics**:
  - `/speak_text_id` (`std_msgs/msg/Int32`): Accepts an ID to determine the text to be spoken.
- **Published Topics**:
  - `/speak` (`std_msgs/msg/String`): Publishes the text corresponding to the ID.

## Example
Publish an ID to the `speak_text_id` topic:
```bash
ros2 topic pub -1 /speak_text_id std_msgs/msg/Int32 "{data: 1}"
```

The corresponding text will be published on the `speak` topic.

## Notes
- Ensure that the `raspicat_speak2` package is installed and operational for speech synthesis.
- Verify the correctness of your `id_to_text.csv` file and its path in the YAML configuration.

## License
[MIT](LICENSE)