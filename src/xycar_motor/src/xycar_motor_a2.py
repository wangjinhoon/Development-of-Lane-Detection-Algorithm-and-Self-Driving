#!/usr/bin/env python
# -*- coding: utf-8 -*-

####################################################################
# 프로그램명 : xycar_motor_a2.py
# 작 성 자 : 자이트론
# 생 성 일 : 2020년 07월 23일
# 본 프로그램은 상업 라이센스에 의해 제공되므로 무단 배포 및 상업적 이용을 금합니다.
####################################################################

import rospy, rospkg
import time
import serial
import threading
from xycar_motor.msg import xycar_motor
from ackermann_msgs.msg import AckermannDriveStamped

import sys
import os
import signal

def signal_handler(sig, frame):
    os.system('killall -9 python rosout')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

angle_offset = 0.0
angle_ratio = 0.0068
speed_ratio = 0.1

def auto_drive(steer_val, car_run_speed):
    global ackerm_publisher
    ack_msg = AckermannDriveStamped()
    ack_msg.header.stamp = rospy.Time.now()
    ack_msg.header.frame_id = ''
    ack_msg.drive.steering_angle = steer_val
    ack_msg.drive.speed = car_run_speed
    ackerm_publisher.publish(ack_msg) 

def callback(data):
    global angle_offset, ackerm_publisher, angle_ratio, speed_ratio

    data.angle = max(-50, min(data.angle, 50))
    data.speed = max(-50, min(data.speed, 50))

    Angle = float(data.angle) * angle_ratio
    Angle += angle_offset * angle_ratio
    Speed = float(data.speed) * speed_ratio

    auto_drive(Angle, Speed)

def start():
    global angle_offset, ackerm_publisher
    rospy.init_node('xycar_motor_a2')
    angle_offset = rospy.get_param("~angle_offset")
 
    rospy.Subscriber("xycar_motor", xycar_motor, callback)
    ackerm_publisher = rospy.Publisher('ackermann_cmd', AckermannDriveStamped, queue_size=1)

    rospy.spin()

if __name__ == '__main__':
    start()
