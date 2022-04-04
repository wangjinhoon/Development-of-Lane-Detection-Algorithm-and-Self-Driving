#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(msg):
    print msg.data
    
rospy.init_node('student')

sub = rospy.Subscriber('my_topic', String, callback)

rospy.spin()
