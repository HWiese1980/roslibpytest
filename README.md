# Demonstration of increasing delay
As mentioned in [issue 41](https://github.com/gramaziokohler/roslibpy/issues/41) of `roslibpy` I'm experiencing an
increasing age of the received messages if the subscriber takes too long to process the received messages, even if
the corresponding queues are configures do be just 1 entry long. 

These scripts demonstrate the behavior

## Launching the demo

Just clone this repo into your catkin workspace's src folder, do a `catkin build` and a `source devel/setup.bash` as 
you would normally do. Then run:

```bash
roslaunch roslibpytest test.launch --screen
```

It should output messages like:

```bash
Age of message:  0.054 seconds
Age of message:  0.544 seconds
Age of message:  1.023 seconds
Age of message:  1.513 seconds
Age of message:  2.003 seconds
Age of message:  2.493 seconds
Age of message:  2.983 seconds
Age of message:  3.474 seconds
Age of message:  3.963 seconds
Age of message:  4.454 seconds
Age of message:  4.944 seconds
Age of message:  5.433 seconds
Age of message:  5.923 seconds
Age of message:  6.412 seconds
Age of message:  6.902 seconds
```

