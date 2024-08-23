#!/usr/bin/env python3
# *-* coding:utf8 *-*


from enum import Enum

class FlowType(Enum):
    avb_a = 0
    avb_b = 1
    be = 2

class Flow(object):
    def __init__(self,
                 id: int,
                 name: str,
                 type: FlowType,
                 src: int,
                 dst: int,
                 size: int,
                 period: int,
                 deadline: int,
                 jitter: int):
        self.id = id
        self.name = name
        self.type = type
        self.src = src
        self.dst = dst
        self.size = size
        self.period = period
        self.deadline = deadline
        self.jitter = jitter
        # self.routing: Optional[Path] = None

    @property
    def rename(self, new_name):
        self.name = new_name

    @property
    def __str__(self):
        # return "["+self.name+"]"
        return "Flow [id = %d, name = %s]" % (self.id, self.name)

    # @property
    # def routing_path(self) -> Path:
    #     if self.routing is None:
    #         raise Exception("Route not set")
    #     return self._routing_path
