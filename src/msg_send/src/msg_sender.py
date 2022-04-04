#!/usr/bin/env python

import rospy
from msg_send.msg import my_msg

rospy.init_node('msg_sender', anonymous=True)

pub = rospy.Publisher('msg_to_xycar', my_msg,queue_size=1)

msg = my_msg()
msg.first_name = "wang"
msg.last_name = "jinhoon"
msg.id_number = 20210815
msg.phone_number = "010-9072-7247"

rate = rospy.Rate(1)

while not rospy.is_shutdown():
	pub.publish(msg)
	print("sending message")
	rate.sleep()
