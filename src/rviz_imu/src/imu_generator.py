#!/usr/bin/env python
#-*-coding:utf-8-*-
# roll, pitch, yaw, value 값은 모두 라디안으로 기록되어 있음
#자세 정보를 롤 피치 요가 아닌 x,y,w 를 담음

import rospy, math, os
from sensor_msgs.msg import Imu
from tf.transformations import quaternion_from_euler

rospy.init_node("imu_generator")
pub = rospy.Publisher("/imu",Imu,queue_size=50)
r = rospy.Rate(5)
f = open("/home/wangjh/xycar_ws/src/rviz_imu/src/imu_data.txt", 'r')
g = []

imu = Imu()
while True:
    line = f.readline()
    if not line: break
    s = line.split(',')
    for i in s:
        l = i.split(':')
        g.append(l) 
    a = float(g[0][1])
    b = float(g[1][1])
    c = float(g[2][1])
    print(a," , ",b," , ",c)
    imu.header.frame_id = "map"
    h = quaternion_from_euler(a,b,c)
    imu.orientation.x = h[0]
    imu.orientation.y = h[1]
    imu.orientation.z = h[2]
    imu.orientation.w = h[3]
    pub.publish(imu) 
    g = []
    r.sleep()

f.close()


#data.txt. 파일에서 한줄씩 읽어다가 

#변환하여 토픽에 담아 밖으로 publish


#모두 다 읽으면 종료