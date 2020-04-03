import logging


def to_epoch(stamp):
    stamp_secs = stamp["secs"]
    stamp_nsecs = stamp["nsecs"]
    return stamp_secs + stamp_nsecs * 1e-9


def from_epoch(stamp):
    stamp_secs = int(stamp)
    stamp_nsecs = (stamp - stamp_secs) * 1e9
    return {"secs": stamp_secs, "nsecs": stamp_nsecs}


def init_logging():
    logger = logging.getLogger("roslibpy")
    handler = logging.StreamHandler()
    logger.addHandler(handler)
