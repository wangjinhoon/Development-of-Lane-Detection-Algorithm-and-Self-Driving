#!/usr/bin/env python
#-*-coding:utf-8-*-
#converter 노드가 보내는 조인트 스태이트 토픽을 받아서 바퀴의
#방향과 회전 속도 정보를 흭득하고
#그 정보를 바탕으로 오도메트리 데이터를 만들어 /odom 토픽에 담아 발행
import math
from math import sin, cos, pi
from sensor_msgs.msg import JointState

import rospy
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3

rospy.init_node('odometry_publisher')
global a
def callback(msg):
    global a
    
    a = msg.position[0] #조향각도
 




odom_pub = rospy.Publisher("/odom", Odometry, queue_size=50)
rospy.Subscriber("joint_states",JointState,callback,queue_size=50)
odom_broadcaster = tf.TransformBroadcaster()
#초기위치 잡기
x = 0.0
y = 0.0


current_time = rospy.Time.now()
last_time = rospy.Time.now()

a = 0
r = rospy.Rate(30)
c_sp = 0.4
wheel_base = 0.2 #축간거리 20센치(앞퀴와 뒷 바퀴 중심간 거리)
yaw = 0

while not rospy.is_shutdown():
    current_time = rospy.Time.now()

    dt = (current_time - last_time).to_sec()

    c_s_a = a
    c_a_v = c_sp*math.tan(c_s_a)/wheel_base # 각속도 = r/v  tan(a) = wheel_base / r d 임으로 wheel_base로 나눠줌

    x_dot = c_sp*cos(yaw)
    y_dot = c_sp*sin(yaw)

    x += x_dot*dt
    y += y_dot*dt
    yaw += c_a_v*dt

    
    # since all odometry is 6DOF we'll need a quaternion created from yaw
    odom_quat = tf.transformations.quaternion_from_euler(0, 0, yaw)

    # first, we'll publish the transform over tf
    odom_broadcaster.sendTransform(
        (x, y, 0.),
        odom_quat,
        current_time,
        "base_link",
        "odom"
    )
    # next, we'll publish the odometry message over ROS
    odom = Odometry()
    odom.header.stamp = current_time
    odom.header.frame_id = "odom"

    # set the position
    odom.pose.pose = Pose(Point(x, y, 0.), Quaternion(*odom_quat))

    # set the velocity
    odom.child_frame_id = "base_link"
    odom.twist.twist = Twist(Vector3(c_sp, c_sp, 0), Vector3(0, 0, yaw))

    # publish the message
    odom_pub.publish(odom)

    last_time = current_time
    r.sleep()
