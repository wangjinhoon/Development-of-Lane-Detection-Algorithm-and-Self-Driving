#!/usr/bin/env python

import rospy
from msg_send.msg import my_msg
from std_msgs.msg import String
import time
import datetime


a = 0

def callback(msg):
    global a
    global time
    global flag
    flag = 1
    a =  str(msg.last_name + msg.first_name)
    time = str(datetime.datetime.now())


    
    
rospy.init_node('teacher', anonymous=True)

sub = rospy.Subscriber('msg_to_xycar', my_msg, callback)
pub = rospy.Publisher('msg_from_xycar',String)

flag = 0

while True:
    if flag == 0:
        continue
    else:
        break

rate = rospy.Rate(2)
rospy.sleep(1)
msg = String()

while not rospy.is_shutdown():
    msg.data = str("good moring, "+ a + " " + time)
    pub.publish(msg)
    rate.sleep()

