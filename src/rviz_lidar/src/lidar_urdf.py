#!/usr/bin/env python
#-*-coding:utf-8-*-

import rospy, time
from std_msgs.msg import Header
from sensor_msgs.msg import Range
from sensor_msgs.msg import LaserScan


lidar_points = None

def lidar_callback(data):
    global lidar_points
    lidar_points = data.ranges
    

rospy.init_node('lidar')
rospy.Subscriber("/scan", LaserScan, lidar_callback, queue_size=1)

pub1 = rospy.Publisher("scan1", Range, queue_size= 1)
pub2 = rospy.Publisher("scan2", Range, queue_size= 1)
pub3 = rospy.Publisher("scan3", Range, queue_size= 1)
pub4 = rospy.Publisher("scan4", Range, queue_size= 1)


msg = Range()
h = Header()

msg.radiation_type = Range().ULTRASOUND
msg.min_range = 0.02
msg.max_range = 2.0
msg.field_of_view = (30.0/180.0)*3.14



while not rospy.is_shutdown():
    if lidar_points == None:
            continue

    h.frame_id = "front"
    msg.header = h
    msg.range = lidar_points[90]
    pub1.publish(msg)

    h.frame_id = "right"
    msg.header = h
    msg.range = lidar_points[180]
    pub2.publish(msg)

    h.frame_id = "back"
    msg.header = h
    msg.range = lidar_points[270]
    pub3.publish(msg)

    h.frame_id = "left"
    msg.header = h
    msg.range = lidar_points[0]
    pub4.publish(msg)


    time.sleep(0.5)