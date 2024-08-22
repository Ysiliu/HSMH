#!/usr/bin/env python3
# *-* coding:utf8 *-*

"""
类别: 基本组件
名称: 任务类
作者: sjjin
邮件: sj_jin@vip.hnist.edu.cn
日期: 2020年3月20日
说明: 重要的组件类
"""
from enum import Enum
from config.config import NUM_QUEUE,NUM_PORT

class NodeType(Enum):
    sw = 0
    es = 1

class Node(int):
    def __init__(self, id: int, type: NodeType) -> None:
        self.id = id
        self.type = type
        self.num_port = NUM_QUEUE
        self.num_queue = NUM_PORT


