#!/usr/bin/env python
#-*-coding:utf-8-*-
import rospy
from xycar_motor.msg import xycar_motor
import time


rospy.init_node('auto_driver', anonymous=True)
pub = rospy.Publisher('/xycar_motor', xycar_motor, queue_size=10)

msg = xycar_motor()

rate = rospy.Rate(1)
  
def motor_pub(msg):
    for i in range(70):
        msg.angle = 50
        msg.speed = 5
        pub.publish(msg)
        time.sleep(0.1)
    
    for i in range(15):
        msg.angle = 0
        msg.speed = 5
        pub.publish(msg)
        time.sleep(0.1)

    for i in range(70):
        msg.angle = -50
        msg.speed = 5
        pub.publish(msg)
        time.sleep(0.1)

    for i in range(15):
        msg.angle = 0
        msg.speed = 5
        pub.publish(msg)
        time.sleep(0.1)

    

while not rospy.is_shutdown():
    motor_pub(msg)
    