from typing import Union
from component.flow import Flow


class Link(object):
    def __init__(self):
        self.node1 = None
        self.port1 = 0
        self.node2 = None
        self.port2 = 0
        self.bandwidth = 100  # 链路带宽
        self.current_flow = []  # 当前正在传输的流
        self.flow_end_time = 0  # 当前流结束传输的时间
        self.flow_not_transmit = 0


    def is_idle(self, time: int) -> bool:
        return time >= self.flow_end_time

    def transmit_flow(self, flow: Flow, time: int):
        if not self.is_idle(time):
            print(f"Link is busy until time {self.flow_end_time}. Cannot transmit flow {flow.name}.")

        # 计算流的传输时间
        # transmission_time = (flow.size * 8) / self.bandwidth  # 秒为单位
        transmission_time = flow.size   # 秒为单位
        self.flow_end_time = time + transmission_time
        self.current_flow.append(flow)
        self.flow_not_transmit = 1
            # 在链路的另一端调用相应的方法，假设是交换机或主机的接收方法
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