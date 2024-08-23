#!/usr/bin/env python3
# *-* coding:utf8 *-*


from enum import Enum
from config.config import MAX_NUM_QUEUE,MAX_NUM_PORT

class NodeType(Enum):
    sw = 0
    es = 1

class Node(int):
    def __init__(self, id: int, type: NodeType) -> None:
        self.id = id
        self.type = type
        self.num_port = MAX_NUM_QUEUE
        self.num_queue = MAX_NUM_PORT


