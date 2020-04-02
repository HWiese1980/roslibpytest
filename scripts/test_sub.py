#!/usr/bin/env python
import roslibpy
import time
import json
import logging
logger = logging.getLogger("roslibpy")
handler = logging.StreamHandler()
logger.addHandler(handler)


def sub(msg):
    # The `age` of the message should remain constant, but it increases seemingly indefinetly
    age = time.time() - to_epoch(msg["stamp"])
    print("Age of message: %6.3f seconds" % age)
    time.sleep(1./5.) # increase if necessary; above a certain loop time the described behavior occurs 


def to_epoch(stamp):
    stamp_secs = stamp["secs"]
    stamp_nsecs = stamp["nsecs"]
    return stamp_secs + stamp_nsecs*1e-9

def from_epoch(stamp):
    stamp_secs = int(stamp)
    stamp_nsecs = (stamp - stamp_secs) * 1e9
    return {"secs": stamp_secs, "nsecs": stamp_nsecs}

ros = roslibpy.Ros("ws://localhost:9090")
ros.run()

ts = roslibpy.Topic(ros, "/test", "std_msgs/Header", queue_length=1)
ts.subscribe(sub)

try:
    while True:
        time.sleep(0)
except KeyboardInterrupt:
    ros.terminate()

