import csv
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class VoiceManager(Node):
    def __init__(self):
        super().__init__('voice_manager')
        
        # Parameters
        self.declare_parameter('id_to_text_csv', '')
        id_to_text_csv = self.get_parameter('id_to_text_csv').value

        # Subscriber
        self.voice_id_sub = self.create_subscription(Int32, 'voice_id', self.voice_id_callback)

        # Load text from CSV file
        self.id_to_text_data = self.load_id_to_text_from_csv(id_to_text_csv)
        if not self.id_to_text_data:
            self.get_logger().error("No id_to_text_data loaded. Please check the CSV file.")

    def load_id_to_text_from_csv(id_to_text_csv):
        pass

    def voice_id_callback(self, msg):
        pass


def main(args=None):
    rclpy.init(args=args)
    node = VoiceManager()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

