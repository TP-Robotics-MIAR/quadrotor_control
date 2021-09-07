#! /home/michael/.local/share/virtualenvs/DeepLearningProject-WE2UAgWf/bin/python


import rospy
from actuate import move
import numpy as np
import sys
from quadrotor_control.msg import ErrorMarker
import math

error_x=0
error_y=0
error_z=0

def callback(data,pid):
    
    global error_x
    global error_y
    global error_z
    
    error = data.Error
    
    if math.sqrt(error[0]**2+error[1]**2+error[2]**2) <= 0.1:
        error_x=0
        error_y=0
        error_z=0
    
    error_x += error[0]
    error_y += error[1]
    error_z += error[2]

    pi = (kp*error[0]+ki*error_x,kp*error[1]+ki*error_y,kp*error[2]+ki*error_z)
    
    try:
        node = move(pi[0],pi[1],pi[2])
        rospy.loginfo([pi[0],pi[1],pi[2]])        
    except rospy.ROSInterruptionException:
        print("Caught Error")





if __name__ == "__main__":
    kp = float(sys.argv[1])
    ki = float(sys.argv[2])
    rospy.init_node("quadrotor_movement", anonymous=True)
    rospy.Subscriber("/target_distance",ErrorMarker,callback,[kp,ki])
    rospy.spin()





