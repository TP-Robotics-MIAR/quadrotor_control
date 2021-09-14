# Quadrotor Control

## Description

This ROS project extrapolates from the ROS package from <https://wiki.ros.org/hector_quadrotor> to create a trajectory following quadcopter. It uses a proportional-integral controller to regulate its acceleration and as such permits a smooth motion.


## Use

First the quadcopter should be instantiated using for example;

```
roslaunch hector_quadrotor_demo outdoor_flight_gazebo.launch
```