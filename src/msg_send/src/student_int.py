#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def callback(msg):
    print msg.data
    
rospy.init_node('student',anonymous=True)

sub = rospy.Subscriber('my_topic', Int32, callback)

rospy.spin()
