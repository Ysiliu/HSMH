#!/usr/bin/env python3
# *-* coding:utf8 *-*



from component.flow import Flow


class RoutingTable:
    def __init__(self):
        self.table = {}

    def add_route(self, dst_addr: int, port_index: int):
        self.table[dst_addr] = port_index

    def get_port_for_flow(self, flow: Flow) -> int:
        return self.table.get(flow.dst, -1)