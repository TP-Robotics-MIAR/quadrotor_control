#! /home/michael/.local/share/virtualenvs/DeepLearningProject-WE2UAgWf/bin/python

import rospy
from std_msgs.msg import Header
from quadrotor_control.msg import ErrorMarker
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseStamped
import numpy as np
import math
import sys
import csv

step = 0
def callback(data):

    global step

    with open('/home/michael/Documents/AIROB/catkin_ws/src/quadrotor_control/scripts/trajectories/square.csv','r') as f:
        pose_from_file = list(csv.reader(f,delimiter=","))
    try:
        pose_config = np.array([list(map(int,i)) for i in pose_from_file])
        error = np.array([
                pose_config[step][0] - data.pose.position.x,
                pose_config[step][1] - data.pose.position.y,
                pose_config[step][2] - data.pose.position.z
            ])
    
        error_magnitude = math.sqrt(error[0]**2 + error[1]**2 + error[2]**2)
    
        if error_magnitude <= 0.1:
            step+=1
    
        rospy.loginfo('Drone at {} ,{}, {} targeting {},{},{}!'.format(data.pose.position.x, data.pose.position.y,data.pose.position.z ,pose_config[step][0],pose_config[step][1],pose_config[step][2]) )
        pub_msg = ErrorMarker()
        pub_msg.header = Header()
        pub_msg.Error = error
        error_pub.publish(pub_msg)
    
    except IndexError:
        rospy.loginfo("Finished Path")

if __name__ == "__main__":
    rospy.init_node("Error", anonymous=True)
    rospy.Subscriber("/ground_truth_to_tf/pose", PoseStamped, callback)
    error_pub = rospy.Publisher("target_distance", ErrorMarker, queue_size=10)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

