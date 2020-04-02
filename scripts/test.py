#!/usr/bin/env python
import roslibpy
import time
import json
import logging
logger = logging.getLogger("roslibpy")
handler = logging.StreamHandler()
logger.addHandler(handler)


def to_epoch(stamp):
    stamp_secs = stamp["secs"]
    stamp_nsecs = stamp["nsecs"]
    return stamp_secs + stamp_nsecs*1e-9

def from_epoch(stamp):
    stamp_secs = int(stamp)
    stamp_nsecs = (stamp - stamp_secs) * 1e9
    return {"secs": stamp_secs, "nsecs": stamp_nsecs}


ros = roslibpy.Ros("ws://localhost:9090")

tt = roslibpy.Topic(ros, "/test", "std_msgs/Header", queue_size=1)
seq = 0

def send_msg():
    print("Send...")
    global seq
    seq += 1
    seq += 1
    header = {"frame_id": "test", "stamp": from_epoch(time.time()), "seq": seq}
    tt.publish(roslibpy.Message(header))
    ros.call_later(0.01, send_msg)

ros.call_later(1, send_msg)
ros.run_forever()
