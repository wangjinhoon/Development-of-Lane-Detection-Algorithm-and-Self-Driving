#!/usr/bin/env python

import rospy, time
from std_msgs.msg import Header
from sensor_msgs.msg import Range
from sensor_msgs.msg import LaserScan


lidar_points = None

def lidar_callback(data):
    global lidar_points
    lidar_points = data.ranges

rospy.init_node('lidar_range', anonymous=True)

pub1 = rospy.Publisher("scan1", Range, queue_size= 1)
pub2 = rospy.Publisher("scan2", Range, queue_size= 1)
pub3 = rospy.Publisher("scan3", Range, queue_size= 1)
pub4 = rospy.Publisher("scan4", Range, queue_size= 1)

rospy.Subscriber("/scan", LaserScan, lidar_callback, queue_size=1)

msg = Range()
h = Header()
h.frame_id = "sensorXY"
msg.header = h
msg.radiation_type = Range().ULTRASOUND
msg.min_range = 0.02
msg.max_range = 2.0
msg.field_of_view = (30.0/180.0)*3.14



while not rospy.is_shutdown():
    msg.header.stamp = rospy.Time.now()

    msg.range = 0.4
    pub1.publish(msg)

    msg.range = 0.8
    pub2.publish(msg)

    msg.range = .12
    pub3.publish(msg)

    msg.range = 1.6
    pub4.publish(msg)

    time.sleep(0.2)