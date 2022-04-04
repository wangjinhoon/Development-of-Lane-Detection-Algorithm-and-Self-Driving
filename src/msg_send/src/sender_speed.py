#!/usr/bin/env python
#-*-coding:utf-8-*-

import rospy
from std_msgs.msg import String

node_name="Sender"
topic_name="long_string"

rospy.init_node(node_name)

pub = rospy.Publisher(topic_name, String,queue_size=1)
msg = String()
rate = rospy.Rate(1)
#1초에 한번 씩

send_str_size = 50000

msg_str = "#"*send_str_size

while not rospy.is_shutdown():
    msg.data = msg_str + ":" + str(rospy.get_time())
    #data에 문장과 그에 따른 시간을 보냄
    pub.publish(msg)
    rate.sleep()
