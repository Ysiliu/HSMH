#!/usr/bin/env python3
# *-* coding:utf8 *-*

"""
类别: 基本组件
作者: sjjin
邮件: sj_jin@vip.hnist.edu.cn
日期: 2022年12月20日
说明: 重要的组件类
"""


from typing import Union
from component.flow import Flow


class Link(object):
    def __init__(self,node1,port1,node2,port2,bandwidth):
        self.node1 = node1
        self.port1 = port1
        self.node2 = node2
        self.port2 = port2
        self.bandwidth = bandwidth
        self.current_flow = []  #the flow sets that transmit on link
        self.flow_end_time = 0
        self.flow_not_transmit = 0


    def is_idle(self, time: int) -> bool:
        return time >= self.flow_end_time

    def transmit_flow(self, flow: Flow, time: int):
        if not self.is_idle(time):
            print(f"Link is busy until time {self.flow_end_time}. Cannot transmit flow {flow.name}.")

        # transmission_time = (flow.size * 8) / self.bandwidth
        transmission_time = flow.size
        self.flow_end_time = time + transmission_time
        self.current_flow.append(flow)
        self.flow_not_transmit = 1

            # if isinstance(self.node2, Host):
            #     return self.node2.flow_in(self.current_flow, time)
            # elif isinstance(self.node2, Switch):
            #     print(f"Flow {flow.name} received by switch {self.node2.name}.")
            #     return self.node2.flow_in(self.current_flow, time)
            # else:
            #     print("Unknown node type for transmission.")
            #     return False


    def __repr__(self):
        return f"Link({self.node1.name}:{self.port1} <--> {self.node2.name}:{self.port2}, bandwidth={self.bandwidth} bps)"

if __name__ == "__main__":
    print(1)