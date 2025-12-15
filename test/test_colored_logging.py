import time

import rclpy
from rclpy.node import Node

rclpy.init()

n = Node('test_logging')

n.get_logger().info('normal')
n.get_logger().info('\033[31m\033[1mbold and red!')
n.get_logger().info('normal again')

n.get_logger().warning('normal')
n.get_logger().warning('\033[31m\033[1mbold and red!')
n.get_logger().warning('normal again')

n.get_logger().error('normal')
n.get_logger().error('\033[31m\033[1mbold and red!')
n.get_logger().error('normal again')

# Ensure the messages make it to rosout before the script dies
time.sleep(1)
