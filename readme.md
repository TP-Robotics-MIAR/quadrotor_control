# Quadrotor Control

## Description

This ROS project extrapolates from the ROS package from <https://wiki.ros.org/hector_quadrotor> to create a trajectory following quadcopter. It uses a proportional-integral controller to regulate its acceleration and as such permits a smooth motion. A PID controller will use the difference(error) between the state of the system; here the quadcopter and of the waypoint to actuate the motors. The proportional value (Kp) will be multiplied with the instantaneous error, the integral value(ki) will be multiplied with the integral value so as to eliminate the steady state error.


## Use

First the quadcopter should be instantiated using for example;

```
roslaunch hector_quadrotor_demo outdoor_flight_gazebo.launch
```

Then the motors should be activate using;

```
rosservice call /enable_motors "enable: true"
```

Afterwards according to the preference of smoothness or speed of motion for the quadcopter you will use the pi controller. First the script for calculating error between the quadcopter and the waypoints. THe waypoints are obtained from a CSV file under the trajectories folder in scripts folder.

```
rosrun quadrotor_control error.py
```

Then to activate the pi controller

```
rosrun quadrotor_control pid.py 0.25 0.0001
```

### Notes

Please ensure at the start of the python files inside the scripts directory, you set the intepreter to your correct python virtual environment directory or use the global python intepreter as such;

```
#!/usr/bin/python
```