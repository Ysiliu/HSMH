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



flow1 = Flow(1, "flow1", FlowType.avb_a, 1001, 1004, 10, 1000, 1000, 0)
flow2 = Flow(2, "flow2", FlowType.avb_b, 1002, 1004, 15, 1000, 1000, 10)
flow3 = Flow(3, "flow3", FlowType.be, 1003, 1004, 40, 1000, 1000, 20)
flow4 = Flow(4, "flow4", FlowType.be, 1003, 1004, 20, 1000, 1000, 0)

# link1=Link(1001,0,2001,0,100,None,0,0,True)

link1=Link()
link1.node1=1001
link1.port1=0
link1.node2=2001
link1.port2=0

ph1=PortHost()
ph1.name='host1_port0'
ph1.addr=1001
ph1.next_addr=2001
ph1.link=link1

host1=Host()
host1.name='host1'
host1.addr=1001
host1.flows.append(flow1)
host1.ports.append(ph1)


##################################


link2=Link()
link2.node1=1002
link2.port1=0
link2.node2=2001
link2.port2=1

ph2=PortHost()
ph2.name='host2_port0'
ph2.addr=1002
ph2.next_addr=2001
ph2.link=link2


host2=Host()
host2.name='host2'
host2.addr=1002
host2.ports.append(ph2)
host2.flows.append(flow2)
##########################

link3=Link()
link3.node1=1003
link3.port1=0
link3.node2=2001
link3.port2=2

ph3=PortHost()
ph3.name='host3_port0'
ph3.addr=1003
ph3.next_addr=2001
ph3.link=link3


host3=Host()
host3.name='host3'
host3.addr=1003
host3.ports.append(ph3)
host3.flows.append(flow3)
host3.flows.append(flow4)

#############################

link4=Link()
link4.node1=2001
link4.port1=3
link4.node2=1004
link4.port2=0

ph4=PortHost()
ph4.name='host4_port0'
ph4.addr=1004
ph4.next_addr=2001
ph4.link=link4


host4=Host()
host4.name='host4'
host4.addr=1004
host4.ports.append(ph4)
#####################################



gcl_data = {
        'start_time': [0, 1000, 2000],
        'end_time': [1000, 2000, 3000],
        'gate_states': [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ]
    }

gcl_df = pd.DataFrame(gcl_data)
 # 设置GCL周期时间
cycle_time = 3000

gcl = GCL()
gcl.cycle_time=3000
gcl.load_gcl_from_dataframe(gcl_df)

##########################################
#交换机入端口0
port0=Port()
port0.name='switch1_port0'
port0.addr=2001
port0.link=link1

#交换机入端口1
port1=Port()
port1.name='switch1_port1'
port1.addr=2001
port1.link=link2

#交换机入端口2
port2=Port()
port2.name='switch1_port2'
port2.addr=2001
port2.link=link3

#交换机出端口3
port3=Port()
port3.name='switch1_port3'
port3.addr=2001
port3.link=link4
port3.gcl=gcl

# #交换机出端口2
# port2=Port()
# port2.name='switch1_port2'
# port2.addr=2001
# port2.link=link4
# port2.gcl=gcl

routetable1=RoutingTable()
routetable1.add_route(1001,0)
routetable1.add_route(1002,1)
routetable1.add_route(1003,2)
routetable1.add_route(1004,3)

switch1=Switch()
switch1.name='switch'
switch1.addr=2001
switch1.num_ports=4
switch1.ports.append(port0)
switch1.ports.append(port1)
switch1.ports.append(port2)
switch1.ports.append(port3)

switch1.routing_table=routetable1

#####################################################



# print(host3.flows)


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

#
#
