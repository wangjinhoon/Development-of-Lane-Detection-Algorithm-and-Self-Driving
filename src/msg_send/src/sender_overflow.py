#!/usr/bin/env python
#-*-coding:utf-8-*-

import rospy
from std_msgs.msg import Int32

node_name="Receiver"
topic_name="my_topic"

rospy.init_node(node_name)

pub = rospy.Publisher(topic_name, Int32)

rate = rospy.Rate(2)

while (pub.get_num_connections() ==0):
    count = 1

while not rospy.is_shutdown():
    pub.publish(count)
    count = count+1
    rate.sleep()