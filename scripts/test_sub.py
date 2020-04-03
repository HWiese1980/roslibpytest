#!/usr/bin/env python
import roslibpy
import time

from common.shared import to_epoch, init_logging
from twisted.internet import reactor

reactor.timeout = lambda: 0.0001

init_logging()

ros = roslibpy.Ros("ws://localhost:9090")
ros.run()


def sub(msg):
    # The `age` of the message should remain constant, but it increases seemingly indefinetly
    age = time.time() - to_epoch(msg["stamp"])
    print("Age of message: %6.3f seconds" % age)
    time.sleep(0.5)  # increase if necessary; above a certain loop time the described behavior occurs


ts = roslibpy.Topic(ros, "/test", "std_msgs/Header", queue_length=1)
ts.subscribe(sub)

try:
    while True:
        time.sleep(0)
except KeyboardInterrupt:
    ros.terminate()
