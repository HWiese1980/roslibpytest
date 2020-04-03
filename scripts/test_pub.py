#!/usr/bin/env python
import roslibpy
import time

from common.shared import from_epoch, init_logging

init_logging()

ros = roslibpy.Ros("ws://localhost:9090")

tt = roslibpy.Topic(ros, "/test", "std_msgs/Header", queue_size=1)
seq = 0


def send_msg():
    global seq
    seq += 1
    seq += 1
    header = {"frame_id": "test", "stamp": from_epoch(time.time()), "seq": seq}
    tt.publish(roslibpy.Message(header))
    ros.call_later(0.01, send_msg)


ros.call_later(1, send_msg)
ros.run_forever()
