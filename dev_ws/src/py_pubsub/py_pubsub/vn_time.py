# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from std_msgs.msg import String


import serial
import time
import os




def vn300(string):
	# print(string)
	data_list = string.decode().split(',')
	# double_list = map(double, data_list)
	
	global Time_vn
	Time_vn = data_list[1]
	# Yaw_vn = data_list[4]
	# Pitch_vn = data_list[5]
	# Roll_vn = data_list[6]
	# Latitude_vn = data_list[7]
	# Altitude_vn = data_list[8]
	
		
	# print("Time_vn " + Time_vn)
	# print("Yaw_vn " + Yaw_vn) 
	# print("Pitch_vn " + Pitch_vn)
	# print("Roll_vn " + Roll_vn)
	# print("Latitude_vn " + Latitude_vn)
	# print("Altitude_vn " + Altitude_vn)
	# print("---------------------------")


class MinimalPublisher(Node):



    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'vn_time', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
    
        vn300(ser.readline())	
        msg = String()
        msg.data = Time_vn
                
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):

    os.system("sudo chmod a+rw /dev/ttyUSB0")
    global ser
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout = 1)
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
