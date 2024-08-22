
import pandas as pd
from component.port import Port
from component.flow import Flow,FlowType
from component.routetable import RoutingTable


class Switch:
    def __init__(self):
        self.name = ''
        self.addr = 0
        self.num_ports = 4
        self.ports = []
        self.routing_table = RoutingTable()
        # self.links = [Link()]
        self.flow_log=[]
    # def flow_in(self, flow: Flow, time: int) -> bool:
    #     port_index = self.routing_table.get_port_for_flow(flow)
    #     if port_index == -1:
    #         print(f"No route found for flow with destination {flow.dst}")
    #         return False
    #     return self.ports[port_index].enqueue(flow)

    def flow_out(self, time:int):
        for i in range(self.num_ports):
            if self.ports[i].link.node1 == self.addr and self.ports[i].link.is_idle(time):
                flow = self.ports[i].dequeue(time)
                if flow != None:
                    self.flow_log.append(f'{self.name}:{self.addr} send {flow.name} at {time}')
                    self.ports[i].link.transmit_flow(flow, time)

    def flow_in(self, time):
        for i in range(self.num_ports):
            if self.ports[i].link.node2 == self.addr:
                if (self.ports[i].link.is_idle(time) and len(self.ports[i].link.current_flow) > 0) or len(self.ports[i].link.current_flow) > 1:
                    flow = self.ports[i].link.current_flow[0]
                    # self.ports[i].link.flow_not_transmit=0
                    del(self.ports[i].link.current_flow[0])
                    port_index = self.routing_table.get_port_for_flow(flow)
                    if port_index != -1:
                        self.flow_log.append(f"{self.name}:{self.addr} received {flow.name} enter port {port_index} at {time}")
                        self.ports[port_index].enqueue(flow)

    def run(self,time:int):
        self.flow_in(time)
        self.flow_out(time)

    def log(self):
        for i in self.flow_log:
            print(i)


if __name__ == "__main__":

    print(1)
    # s = Switch()
    # s.ports[0].addr = 1002
    # s.routing_table.add_route(1002,0)
    #
    # gcl_data = {
    #         'start_time': [0, 1000, 2000],
    #         'end_time': [1000, 2000, 3000],
    #         'gate_states': [
    #             [1, 0, 0, 1],
    #             [0, 1, 0, 0],
    #             [0, 0, 1, 0],
    #         ]
    #     }
    # gcl_df = pd.DataFrame(gcl_data)
    # s.ports[0].gcl.load_gcl_from_dataframe(gcl_df)
    # s.ports[0].gcl.cycle_time=3000
    #
    # f1 = Flow(1, "Flow1", FlowType.avb_a, 1000, 1002, 100, 1000, 2000, 10)
    #
    # # s.flow_in(f1)
    # # s.flow_out(10)
