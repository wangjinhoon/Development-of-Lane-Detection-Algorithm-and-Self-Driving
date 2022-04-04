#!/usr/bin/env python

import rospy, math, os
from sensor_msgs.msg import Imu
from tf.transformations import euler_from_quaternion, quaternion_from_euler

degrees2rad = float(math.pi)/float(180.0)
rad2degrees = float(180.0)/float(math.pi)
name = " >> ./data.txt"

def listener():
  rospy.init_node('imu_output', anonymous=False)
  rospy.Subscriber('imu', Imu, call_back)

def call_back(data):
  global degrees2rad
  global rad2degrees

  euler = euler_from_quaternion((data.orientation.x, data.orientation.y, data.orientation.z, data.orientation.w))
  euler = [euler[0],euler[1],euler[2]] 
  save_str = "roll : " + str(euler[0]) + ", " + "pitch : " + str(euler[1]) + ", " + "yaw : " + str(euler[2])
  command = 'echo "' + save_str + '" >> ./data.txt'
  print(command)
  os.system(command)

if __name__ == '__main__':
  listener()
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
