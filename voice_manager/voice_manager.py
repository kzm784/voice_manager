import csv
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String

class VoiceManager(Node):
    def __init__(self):
        super().__init__('voice_manager')
        self.declare_parameter('id_to_text_csv', '')
        id_to_text_csv = self.get_parameter('id_to_text_csv').value
        self.voice_id_sub = self.create_subscription(Int32, 'speak_text_id', self.voice_id_callback, 10)
        self.text_pub = self.create_publisher(String, 'speak', 10)

        try:
            self.id_to_text_data = self.load_id_to_text_from_csv(id_to_text_csv)
        except Exception as e:
            self.get_logger().error(f"Failed to load CSV: {e}")
            self.id_to_text_data = {}

    def load_id_to_text_from_csv(self, id_to_text_csv):
        id_to_text = {}
        with open(id_to_text_csv, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                id_to_text[int(row['id'])] = row['text']
        return id_to_text

    def voice_id_callback(self, msg):
        text = self.id_to_text_data.get(msg.data, "対応するテキストが見つかりません")
        self.get_logger().info(f"Voice ID: {msg.data}, Text: {text}")
        text_msg = String()
        text_msg.data = text
        self.text_pub.publish(text_msg)

def main(args=None):
    rclpy.init(args=args)
    node = VoiceManager()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
