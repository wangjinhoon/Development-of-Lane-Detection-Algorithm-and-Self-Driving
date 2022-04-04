#!/usr/bin/env python
#-*-coding:utf-8-*-

import rospy
from std_msgs.msg import Int32

rospy.init_node('sender_serial')

pub = rospy.Publisher('my_topic', Int32)

rate = rospy.Rate(2)


"""
while count == 1:
    pub.publish(count)
    count += 1

"""


while (pub.get_num_connections() ==0):
    count = 1
##노드가연결되면 노드 갯수를 리턴하는 함수 그러므로 노드가 연결되면 루프문을 나온다.
##이것으로 알 수 있는건 아마 노드가 연결되지 않아도 값을 보내는 것 같다


while not rospy.is_shutdown():
    pub.publish(count)
    rate.sleep()
    count = count+1
    
