#!/usr/bin/env python3
# *-* coding:utf8 *-*

"""
类别: 基本组件
作者: sjjin
邮件: sj_jin@vip.hnist.edu.cn
日期: 2022年12月20日
说明: 重要的组件类
"""

from component.port import PortHost,Port
from component.flow import Flow
from component.routetable import RoutingTable
from component.link import Link


class Host:
    def __init__(self,name:str,addr:int,ports:[],flows:[]):
        self.addr = addr
        self.name = name
        self.num_ports = 1
        self.routing_table = RoutingTable()
        self.ports = ports
        # self.port = PortHost()
        self.flows = flows
        # self.links = [Link()]
        self.flow_log=[]
    # def flow_in(self, flow: Flow, time:int) -> bool:
    #     print(f"{self.name} received flow {flow.name} at {time}")
    #     return True

    def flow_in(self, time):
        for i in range(self.num_ports):
            if self.ports[i].link.node2 == self.addr :
                if (self.ports[i].link.is_idle(time) and len(self.ports[i].link.current_flow) > 0) or len(self.ports[i].link.current_flow) > 1 :
                    flow = self.ports[i].link.current_flow[0]
                    del(self.ports[i].link.current_flow[0])
                    # self.ports[i].link.flow_not_transmit = 0
                    self.flow_log.append(f"{self.name}:{self.addr} received {flow.name} at {time}")
                    # return True
            # return False

    def flow_in_port(self,time: int):
        for flow in self.flows:
            if (time % flow.period) - flow.jitter == 0:
                self.ports[0].enqueue(flow)


    def flow_out(self, time: int):
        if len(self.flows) == 0:
            return False
        for i in range(self.num_ports):
            if self.ports[i].link.node1 == self.addr and self.ports[i].link.is_idle(time):
                flow = self.ports[i].dequeue(time)
                if flow != None:
                    self.flow_log.append(f'{self.name}:{self.addr} send {flow.name} at {time}')
                    self.ports[i].link.transmit_flow(flow, time)

        # for flow in self.flows:
        #     if (time - flow.jitter) % flow.period == 0:
        #         port_index = self.routing_table.get_port_for_flow(flow)
        #         if port_index == -1:
        #             print(f"No route found for flow with destination {flow.dst}")
        #             return False
        #         else:
        #             if self.links[port_index].is_idle(time):
        #                     return self.links[port_index].transmit_flow(flow,time)

    def run(self,time:int):
        self.flow_in(time)
        self.flow_in_port(time)
        self.flow_out(time)

    def log(self):
        for i in self.flow_log:
            print(i)


    def __repr__(self):
        return f"Host(addr={self.addr}, name={self.name})"