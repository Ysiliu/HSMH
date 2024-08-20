#!/usr/bin/env python3
# *-* coding:utf8 *-*

"""
类别: 基本组件
名称: 任务类
作者: siliu
邮件: sj_jin@vip.hnist.edu.cn
日期: 2020年3月20日
说明: 重要的组件类
"""

class FlowSet(object):
    def __init__(self, set_type):
        self.set_type = set_type
        self.flows = []

    def __str__(self):
        return "Set [set_type = %s, flows = %s]" % (self.set_type, self.flows)
     
    def __length__(self) -> int:
        return len(self.flows)

    def get_flow(self, flow:int):
        return self.flows[int(flow)]

    def get_flows(self):
        return self.flows


