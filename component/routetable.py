from component.flow import Flow


class RoutingTable:
    def __init__(self):
        # 初始化一个空的路由表，字典格式，key 是目标地址，value 是端口号
        self.table = {}

    def add_route(self, dst_addr: int, port_index: int):
        self.table[dst_addr] = port_index

    def get_port_for_flow(self, flow: Flow) -> int:
        # 如果找到目的地址对应的端口号则返回，否则返回 -1 表示未找到
        return self.table.get(flow.dst, -1)