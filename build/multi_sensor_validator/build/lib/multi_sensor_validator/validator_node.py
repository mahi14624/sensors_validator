import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String
from multi_sensor_validator.validator import Validator


class ValidatorNode(Node):

    def __init__(self):
        super().__init__('validator_node')

        self.validator = Validator(threshold=20)

        self.ultrasonic_value = None
        self.infrared_value = None

        self.create_subscription(Int32, '/ultrasonic_range', self.ultrasonic_callback, 10)
        self.create_subscription(Int32, '/infrared_range', self.infrared_callback, 10)

        self.result_pub = self.create_publisher(String, '/validation_result', 10)

    def ultrasonic_callback(self, msg):
        self.ultrasonic_value = msg.data
        self.try_publish()

    def infrared_callback(self, msg):
        self.infrared_value = msg.data
        self.try_publish()

    def try_publish(self):
        if self.ultrasonic_value is None or self.infrared_value is None:
            return

        result = self.validator.validate(self.ultrasonic_value, self.infrared_value)

        out = String()
        out.data = f"Ultrasonic: {self.ultrasonic_value} cm, Infrared: {self.infrared_value} cm -> {result}"
        self.result_pub.publish(out)


def main(args=None):
    rclpy.init(args=args)
    node = ValidatorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()




if __name__ == '__main__':
    main()