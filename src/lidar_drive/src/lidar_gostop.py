#!/usr/bin/env python
​
import rospy
import time
from sensor_msgs.msg import LaserScan
from xycar_msgs.msg import xycar_motor
​
motor_msg=xycar_motor()
distance=[]
​
#라이다 토픽이 들어오면 실행
def callback(data):
    global distance
    global motor_msg
    distance=data.ranges
​
#자동차 전진(장애물 없으면)
def drive_go():
    global  motor_msg
    motor_msg.speed=5
    motor_msg.angle=0
    pub.publish(motor_msgs)
#자동차 정지(장애물 있으면)
def drive_stop():
    global motor_msg
    motor_msg.speed=0
    motor_msg.angle=0
    pub.publish(motor_msgs)
rospy.init_node('lidar_driver')
rospy.Subscriber("/scan", LaserScan, callback, queue_size=1)
pub = rospy.Publisher('xycar_motor',xycar_motor, queue_size=1)
time.sleep(3) #라이다 켜지기  기다림
while not rospy.is_shutdown():
    ok = 0
    for degree in range(60,120):
        if distance[degree] <= 0.3:
            ok +=1
        if ok > 3:
            drive_stop()
            break
    if ok <=3:
        drive_go()
    
    