#!/usr/bin/env python

import rospy
from xycar_motor.msg import xycar_motor


rospy.init_node('auto_driver', anonymous=True)
pub = rospy.Publisher('/xycar_motor', xycar_motor, queue_size=10)

msg = xycar_motor()

rate = rospy.Rate(1)
  
def motor_pub(msg):
    for i in range(0,5):
        msg.angle = 30
        msg.speed = 3
        pub.publish(msg)
    
    for i in range(0,5):
        msg.angle = 0
        msg.speed = 3
        pub.publish(msg)

    for i in range(0,5):
        msg.angle = -30
        msg.speed = 3
        pub.publish(msg)

    for i in range(0,5):
        msg.angle = 0
        msg.speed = 3
        pub.publish(msg)
    

while not rospy.is_shutdown():
    motor_pub(msg)
    rate.sleep()