import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from multi_sensor_validator.sensors import Infrared

class InfraredNode(Node):
    def __init__(self):
        super().__init__('infrared_node')

        self.sensor = Infrared(min_range=10, max_range=200)
        self.publisher_ = self.create_publisher(Int32, '/infrared_range', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)  # 1 Hz

    def timer_callback(self):
        msg = Int32()
        msg.data = self.sensor.read_distance()
        self.publisher_.publish(msg)
        self.get_logger().info(f'Infrared: {msg.data} cm')

def main(args=None):
    rclpy.init(args=args)
    node = InfraredNode()
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