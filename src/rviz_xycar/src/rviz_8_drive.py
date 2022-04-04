#!/usr/bin/env python

import rospy
from xycar_motor.msg import xycar_motor


rospy.init_node('auto_driver', anonymous=True)
pub = rospy.Publisher('/xycar_motor', xycar_motor, queue_size=10)

msg = xycar_motor()

rate = rospy.Rate(50)
  
def motor_pub(msg):
    for i in range(0,5):
        msg.angle = 8
        msg.speed = 0.5
        pub.publish(msg)
        rate.sleep()

    
    for i in range(0,5):
        msg.angle = 0
        msg.speed = 0.5
        pub.publish(msg)
        rate.sleep()

    for i in range(0,5):
        msg.angle = -8
        msg.speed = 0.5
        pub.publish(msg)
        rate.sleep()

    for i in range(0,5):
        msg.angle = 0
        msg.speed = 0.5
        pub.publish(msg)
        rate.sleep()
    

while not rospy.is_shutdown():
    motor_pub(msg)
    rate.sleep()