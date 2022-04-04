#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from xycar_motor.msg import xycar_motor
import math

def talker():
    global a
    global b
    global c
    global d 
    global v

    def callback(msg):
        global a
        global b
        global c
        global d 
        global v
        c = msg.angle
        d = math.radians(c * 0.4)
        v = msg.speed
        hello_xycar.header.stamp = rospy.Time.now()
      
        if a >= 3.14:
            a = -3.14
            b = -3.14
        else:
            a += 0.6
            b += 0.6

        

        hello_xycar.position = [d, d, a, b, a, b]
        hello_xycar.velocity = [v]
        pub.publish(hello_xycar)
        rate.sleep()

    rospy.Subscriber('/xycar_motor',xycar_motor,callback,queue_size=10)
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('converter')
    rate = rospy.Rate(5) 

    hello_xycar = JointState()
    hello_xycar.header = Header()
    hello_xycar.name = ['front_right_hinge_joint', 'front_left_hinge_joint', 
                      'front_right_wheel_joint', 'front_left_wheel_joint',
                       'rear_right_wheel_joint','rear_left_wheel_joint']
    hello_xycar.velocity = []
    hello_xycar.effort = [] 
  
    a = -3.14
    b = -3.14
    c = 0
    d = 0

    rospy.spin()


      

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass