#!/usr/bin/env python
#-*-coding:utf-8-*-

import rospy
from std_msgs.msg import Int32

node_name="Sender"
topic_name="my_topic"

def callback(msg):
    rospy.loginfo("callback ~ing")
    load_size = 10   #부하갯수 
    for i in range(load_size):  #부하 반복
        rospy.sleep(1)
    print msg.data

    
rospy.init_node(node_name)

sub = rospy.Subscriber(topic_name, Int32, callback)

rospy.spin()

"""
큐 사이즈가 1 일 경우 부하를 주었을때 토픽이 6~7개씩 누락되는 것을 볼 수 있었다.

큐 사이즈를 1 -> 100으로 늘리거나 큐 사이즈를 적지 않으면 누락되는것이 없는 것을 볼 수 있엇다.

제일 좋은 방법은 구독자의 부하를 없애는 방법임을 알 수 있었다.
"""
