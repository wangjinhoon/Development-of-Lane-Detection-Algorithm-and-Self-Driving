#!/usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node('teacher')

pub = rospy.Publisher('my_topic', String)

rate = rospy.Rate(2)

while not rospy.is_shutdown():
    pub.publish('call me please')
    rate.sleep()
