#! /home/michael/.local/share/virtualenvs/DeepLearningProject-WE2UAgWf/bin/python

import rospy
from geometry_msgs.msg import Twist


def move(x_vel, y_vel, z_vel):

    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(5)
    vel = Twist()

    vel.linear.x = x_vel
    vel.linear.y = y_vel
    vel.linear.z = z_vel

    pub.publish(vel)

    #rate.sleep()
