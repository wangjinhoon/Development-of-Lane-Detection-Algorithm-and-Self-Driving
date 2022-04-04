#!/usr/bin/env python

import rospy
from std_msgs.msg import String

node_name="receiver"

def callback(msg):
    print msg.data
    
rospy.init_node(node_name)

sub = rospy.Subscriber("msg_to_receiver" , String, callback)
pub = rospy.Publisher("center",String, queue_size=1)

rate=rospy.Rate(10)
rospy.sleep(1)
order=["first","second","third","fourth"]

pub_msg= String()

for i in order:
    pub_msg.data = i
    pub.publish(pub_msg)
    rospy.sleep(3)

rospy.spin()