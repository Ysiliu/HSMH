#!/usr/bin/env python3
# *-* coding:utf8 *-*

from component.flow import Flow,FlowType
from enum import Enum
import random
from typing import List
def generate_random_flows(num_flows: int,
                          type_range: List[FlowType],
                          period_range: List[int],
                          deadline_range: List[int],
                          jitter_range: List[int],
                          size_range: List[int],
                          src_range: List[int],
                          dst_range: List[int]) -> List[Flow]:
    flows = []
    for i in range(num_flows):
        flow_id = i + 1
        name = f"Flow_{flow_id}"
        flow_type = random.choice(type_range)
        period = random.randint(period_range[0], period_range[1])
        deadline = random.randint(deadline_range[0], deadline_range[1])
        jitter = random.randint(jitter_range[0], jitter_range[1])
        size = random.randint(size_range[0], size_range[1])
        src = random.randint(src_range[0], src_range[1])
        dst = random.randint(dst_range[0], dst_range[1])

        flow = Flow(flow_id, name, flow_type, src, dst, size, period, deadline, jitter)
        flows.append(flow)
    return flows

flows = generate_random_flows(
    num_flows=10,
    type_range=[FlowType.avb_a, FlowType.avb_b, FlowType.be],
    period_range=[500, 2000],
    deadline_range=[1000, 4000],
    jitter_range=[0, 100],
    size_range=[100, 1000],
    src_range=[1, 10],
    dst_range=[1, 10]
)

for flow in flows:
    print(flow.__str__)
