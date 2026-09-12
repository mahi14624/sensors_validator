
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Logger:

    def log(self, message: str) -> None:
        print(message)


class LoggerNode(Node):

    def __init__(self):
        super().__init__('logger_node')
        self.logger_obj = Logger()
        self.subscription = self.create_subscription(
            String, '/validation_result', self.callback, 10)

    def callback(self, msg: String):
        self.logger_obj.log(msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = LoggerNode()
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