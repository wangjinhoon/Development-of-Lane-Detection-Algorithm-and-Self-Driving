#!/usr/bin/env python

import rospy
from msg_send.msg import my_msg
from std_msgs.msg import String

rospy.init_node('student', anonymous=True)

def callback(msg):
    print(msg.data)

pub = rospy.Publisher('msg_to_xycar', my_msg,queue_size=1)
sub = rospy.Subscriber('msg_from_xycar',String)

msg = my_msg()
msg.first_name = "jinhoon"
msg.last_name = "wang"
msg.id_number = 20210815
msg.phone_number = "010-9072-7247"

rate = rospy.Rate(1)

while not rospy.is_shutdown():
	pub.publish(msg)
	rate.sleep()
