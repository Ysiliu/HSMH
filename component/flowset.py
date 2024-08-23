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
import pandas as pd
from typing import List, Optional
from enum import Enum
from component.flow import Flow,FlowType


class FlowSet:
    def __init__(self):
        self.flows: List[Flow] = []

    def add_flow(self, flow: Flow):
        self.flows.append(flow)

    def remove_flow(self, flow_id: int) -> bool:
        for flow in self.flows:
            if flow.id == flow_id:
                self.flows.remove(flow)
                return True
        return False

    def get_flow_by_id(self, flow_id: int) -> Optional[Flow]:
        for flow in self.flows:
            if flow.id == flow_id:
                return flow
        return None

    def get_flows_by_type(self, flow_type: FlowType) -> List[Flow]:
        return [flow for flow in self.flows if flow.type == flow_type]

    def get_all_flows(self) -> List[Flow]:
        return self.flows

    def __iter__(self):
        return iter(self.flows)

    def __len__(self):
        return len(self.flows)

    def __str__(self):
        return f"FlowSet with {len(self.flows)} flows"

    def from_csv(cls, filepath: str) -> 'FlowSet':

        df = pd.read_csv(filepath)
        flow_set = cls()

        for _, row in df.iterrows():
            flow = Flow(
                id=int(row['id']),
                name=str(row['name']),
                type=FlowType(row['type']),
                src=int(row['src']),
                dst=int(row['dst']),
                size=int(row['size']),
                period=int(row['period']),
                deadline=int(row['deadline']),
                jitter=int(row['jitter'])
            )
            flow_set.add_flow(flow)

        return flow_set

if __name__ == "__main__":

    flow_set = FlowSet.from_csv('flows.csv')
    print(flow_set)