#!/usr/bin/env python3
# *-* coding:utf8 *-*

"""
作者: sjjin
邮件: sj_jin@vip.hnist.edu.cn
日期: 2022年12月20日
"""

from typing import List
import pandas as pd
from component.gcl import GCL
from component.flow import Flow,FlowType
from component.routetable import RoutingTable
from component.node import Node,NodeType
from component.link import Link
from component.host import Host
from component.port import PortHost,Port
from component.switch import Switch
from component.fifoqueue import FifoQueue


flow1 = Flow(1, "flow1", FlowType.avb_a, 1001, 1004, 10, 1000, 1000, 0)
flow2 = Flow(2, "flow2", FlowType.avb_b, 1002, 1004, 15, 1000, 1000, 10)
flow3 = Flow(3, "flow3", FlowType.be, 1003, 1004, 40, 1000, 1000, 20)
flow4 = Flow(4, "flow4", FlowType.be, 1003, 1004, 20, 1000, 1000, 0)

link1=Link(1001,0,2001,0,100)
ph0=PortHost('host1_port0',1001,2001,link1)
host1=Host('host1',1001,[ph0],[flow1])

link2=Link(1002,0,2001,1,100)
ph1=PortHost('host2_port0',1002,2001,link2)
host2=Host('host2',1002,[ph1],[flow2])

link3=Link(1003,0,2001,2,100)
ph2=PortHost('host3_port0',1003,2001,link3)
host3=Host('host3',1003,[ph2],[flow3,flow4])

link4=Link(2001,3,1004,0,100)
ph3=PortHost('host4_port0',1004,2001,link4)
host4=Host('host4',1004,[ph3],[])

gcl_data = {
        'start_time': [0, 1000, 2000, 3000],
        'end_time': [1000, 2000, 3000, 4000],
        'gate_states': [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 1, 1],
            [1, 1, 1, 1]
        ]
    }

gcl_df = pd.DataFrame(gcl_data)

gcl = GCL()
gcl.cycle_time=4000
gcl.load_gcl_from_dataframe(gcl_df)

port0=Port('switch1_port0',2001,1001,None,link1)
port1=Port('switch1_port1',2001,1002,None,link2)
port2=Port('switch1_port2',2001,1003,None,link3)
port3=Port('switch1_port3',2001,1004,gcl,link4)
port3.queues=[FifoQueue(1000),FifoQueue(1000),FifoQueue(1000),FifoQueue(1000)]
port3.thresholdvalue=0

routetable1=RoutingTable()
routetable1.add_route(1001,0)
routetable1.add_route(1002,1)
routetable1.add_route(1003,2)
routetable1.add_route(1004,3)

switch1=Switch('switch1',2001,[port0,port1,port2,port3],routetable1)


#####################################################


t=0

while t<20000:
    host1.run(t)
    host2.run(t)
    host3.run(t)
    switch1.run(t)
    host4.run(t)
    t=t+1


host1.log()
host2.log()
host3.log()
host4.log()
switch1.log()
