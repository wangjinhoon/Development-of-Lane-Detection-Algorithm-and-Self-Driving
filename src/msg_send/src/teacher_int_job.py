#!/usr/bin/env python
#-*-coding:utf-8-*-

import rospy
from std_msgs.msg import Int32
import timeit

node_name="teacher"
topic_name="msg_to_students"

rospy.init_node(node_name,anonymous =True)
pub = rospy.Publisher(topic_name, Int32, queue_size=1)


def do_job(num):
    for i in range(num):
        i=i+1
        pub.publish(i)
    
r = input('input rate > ')
rate = rospy.Rate(r)
num = input('input counter num > ')

total = 0


for j in range(r):
    start_send = timeit.default_timer()
    do_job(num)
    end_send = timeit.default_timer()
    send = end_send - start_send
    rospy.loginfo("Send time : " + str(send))
    rate.sleep()
    end_sleep = timeit.default_timer()
    sleep = end_sleep - end_send
    rospy.loginfo("sleep time : " + str(sleep))
    rospy.loginfo("send+sleep : " + str(send + sleep))
    total += (send+ sleep)
    rospy.loginfo(" ")

rospy.loginfo("total : " + str(total))

"""
r = 5 num = 10000 일때는 send 시간이 0.4초 정도로 sleeptime 은 0.16초 정도였다. 
r = 5 num = 1000000 일때는 처리가 너무 오래 걸려 하나를 처리 하는데 3초 이상 걸렸고 sleep time은 0.001초로 거의 없다 싶이 했다. 총합 15초 걸렸다.

r = 10 0.1초 num = 10000 일때 잘 처리 하는 것을 볼수 있다

r = 100 0.01초 num = 10000 sleep 타임이 0.001초로 거의 없다 싶이 하는것을 알 수 있었다.

r = 5000 num = 10000 send 시간은 0.03초 정도 걸리고 sleep 타임은 0.001초 정도로 거의 없었다.

하지만 전체적으로 너무 빨라서 그런지 1~num 까지의 숫자를 전부 나열하지는 못하는 것을 알 수 있었다.

"""
