#!/usr/bin/env python
#-*-coding:utf-8-*-
import rospy
from std_msgs.msg import String
import time

node_name="Receiver"
topic_name="long_string"

def callback(msg):
    new_time = str(rospy.get_time())
    #현재 시간을 문자열로 변환하여 저장한다.
    received_data = str(msg.data).split(":")
    # : 기준으로 잘라 저장
    during_time = float(new_time) - float(received_data[1])
    #현재시간과 받은시간의 차를 구함
    str_size = len(received_data[0])
    rospy.loginfo(str(str_size) + "byte" + str(during_time) + "second")
    if during_time != 0:
        rospy.loginfo("speed" + str(float(str_size)/during_time) + "byte/s")

    
rospy.init_node(node_name)

sub = rospy.Subscriber(topic_name, String, callback)

rospy.spin()

"""
값이 커질수록 받는데 시간이 오래걸리는것을 확인 할 수 있었다.
"""