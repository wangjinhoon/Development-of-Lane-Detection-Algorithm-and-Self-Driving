#!/usr/bin/env python
#-*-coding:utf-8-*-
import rospy
from std_msgs.msg import String

flag = 0

def callback(msg):
    global flag
    flag = str(msg.data)

rospy.init_node("fouth")
rospy.Subscriber("center",String,callback)
while True:
    if flag == 0:
        continue
    elif flag == "fourth":
        break
pub =rospy.Publisher("msg_to_receiver", String, queue_size=1)
rate = rospy.Rate(2)
msg_str = String()
while not rospy.is_shutdown():
    msg_str.data = " this is fourth "
    pub.publish(msg_str)
    rate.sleep()