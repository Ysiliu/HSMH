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

from typing import List, Tuple
from enum import Enum
from config.config import MAX_NUM_QUEUE

import pandas as pd


class GateState(Enum):
    OPEN = 1
    CLOSED = 0


class GCL:
    def __init__(self):
        self.gcl_entries = []
        self.cycle_time = 3000
        self.is_guard= False
        self.guard_time=[(0,100,[1,1,1,1])]

    def load_gcl_from_dataframe(self, gcl_df: pd.DataFrame):
        for _, row in gcl_df.iterrows():
            start_time = row['start_time']
            end_time = row['end_time']
            gate_states = [GateState(state) for state in row['gate_states']]
            self.gcl_entries.append((start_time, end_time, gate_states))

    def get_gate_state_at_time(self, time: int):
        time_in_cycle = time % self.cycle_time

        for start_time, end_time, gate_states in self.gcl_entries:
            if start_time <= time_in_cycle < end_time:
                return gate_states
        return None

    def is_queue_open(self, time: int, queue_index: int) -> bool:
        gate_states = self.get_gate_state_at_time(time)
        if gate_states is None:
            return False
        return gate_states[queue_index] == GateState.OPEN


if __name__ == "__main__":

    gcl_data = {
        'start_time': [0, 1000, 2000],
        'end_time': [1000, 2000, 3000],
        'gate_states': [
            [1, 0, 0, 1],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
        ]
    }


    gcl_df = pd.DataFrame(gcl_data)
    cycle_time = 3000

    gcl = GCL()
    gcl.cycle_time=3000
    gcl.load_gcl_from_dataframe(gcl_df)

    state_at_3500 = gcl.get_gate_state_at_time(3500)
    # state_str = ''.join(['O' if state == GateState.OPEN else 'C' for state in state_at_3500])

    print(f"At time=3500, the gate state is: {state_at_3500}")
    print(f"At time=3500, the gate state is: {gcl.is_queue_open(3500,0)}")
    print(gcl.gcl_entries[0])
    print(gcl.guard_time)