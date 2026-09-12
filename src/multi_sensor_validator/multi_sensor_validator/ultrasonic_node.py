import rclpy
from rclpy.node import Node
from multi_sensor_validator.sensors import Ultrasonic_sensor

class UltrasonicNode(Node):
    def __init__(self):
        super().__init__('_node')

        self.sensor = Ultrasonic_sensor(min_range=10, max_range=200)
        self.publisher_ = self.create_publisher(Int32, '/ultrasonic_range', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)  # 1 Hz

    def timer_callback(self):
        msg = Int32()
        msg.data = self.sensor.read()
        self.publisher_.publish(msg)
        self.get_logger().info(f'Ultrasonic: {msg.data} cm')


def main(args=None):
    rclpy.init(args=args)
    node = UltrasonicNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()   