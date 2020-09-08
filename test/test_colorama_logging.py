import rclpy
from rclpy.node import Node
import colorama
from colorama import Fore, Style, init

rclpy.init()

n = Node('test_logging')

colorama.init(autoreset=True)

n.get_logger().info("normal")
n.get_logger().info(Fore.RED + Style.BRIGHT + "bold and red!")
n.get_logger().info("normal again")

n.get_logger().warning("normal")
n.get_logger().warning(Fore.RED + Style.BRIGHT + "bold and red!")
n.get_logger().warning("normal again")

n.get_logger().error("normal")
n.get_logger().error(Fore.RED + Style.BRIGHT + "bold and red!")
n.get_logger().error("normal again")
