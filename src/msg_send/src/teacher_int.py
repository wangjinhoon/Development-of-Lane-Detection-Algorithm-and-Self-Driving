#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

rospy.init_node('teacher',anonymous =True)

pub = rospy.Publisher('my_topic', Int32)

rate = rospy.Rate(2)
count = 1

while not rospy.is_shutdown():
    pub.publish(count)
    count = count+1
    rate.sleep()
