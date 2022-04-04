#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

def talker():
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('move_joint')
    rate = rospy.Rate(50) 

    hello_xycar = JointState()
    hello_xycar.header = Header()
    hello_xycar.name = ['front_right_hinge_joint', 'front_left_hinge_joint', 
                      'front_right_wheel_joint', 'front_left_wheel_joint',
                       'rear_right_wheel_joint','rear_left_wheel_joint']
    hello_xycar.velocity = []
    hello_xycar.effort = [] 
  
    a = -3.14
    b = -3.14

    while not rospy.is_shutdown():
      hello_xycar.header.stamp = rospy.Time.now()
      
      if a >= 3.14:
         a = -3.14
         b = -3.14
      else:
         a += 0.01
         b += 0.01

      hello_xycar.position = [0, 0, a, b, 0, 0]

      pub.publish(hello_xycar)
      rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass


