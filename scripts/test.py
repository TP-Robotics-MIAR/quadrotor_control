#! /home/michael/.local/share/virtualenvs/DeepLearningProject-WE2UAgWf/bin/python

import rospy
from std_msgs.msg import Header
from deep_mpc.msg import ErrorMarker
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseStamped
import numpy as np
import sys

import csv
import numpy as np
 
with open('./trajectories/square.csv', 'r') as f:
    data = list(csv.reader(f, delimiter=","))
       
data = np.array([list(map(int,i)) for i in data])
print(data)
