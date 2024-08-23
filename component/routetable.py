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



from component.flow import Flow


class RoutingTable:
    def __init__(self):
        self.table = {}

    def add_route(self, dst_addr: int, port_index: int):
        self.table[dst_addr] = port_index

    def get_port_for_flow(self, flow: Flow) -> int:
        return self.table.get(flow.dst, -1)