from component.flow import Flow,FlowType
from component.fifoqueue import FifoQueue
from component.heapqueue import EDFHeapQueue,STFHeapQueue
from config.config import ThresholdValue
from component.gcl import GCL
from typing import Optional
from component.link import Link


class Port:
    def __init__(self):
        self.name = ''
        self.next_addr = 0
        self.addr = 0
        self.num_queue = 4  # HSMH中队列设置为4
        self.queues = [EDFHeapQueue(1000), EDFHeapQueue(1000),FifoQueue(1000), STFHeapQueue(1000)]
        self.gcl = GCL()
        self.link = Link()
        self.in_queue=FifoQueue(1000)

    def enqueue(self, flow: Flow):
        if flow.type == FlowType.avb_a:
            self.queues[0].enqueue(flow)
        elif flow.type == FlowType.avb_b:
            self.queues[1].enqueue(flow)
        elif flow.type == FlowType.be:
            if flow.size <=  ThresholdValue:
                self.queues[3].enqueue(flow)
            else:
                self.queues[2].enqueue(flow)
        else:
            print(f"Unknown flow type: {flow.type}")
            return False

    def dequeue(self, time: int) -> Optional[Flow]:
        for i in range(self.num_queue):
            if self.gcl.is_queue_open(time, i) and not self.queues[i].is_empty():
                return self.queues[i].dequeue()
        return None

class PortHost:
    def __init__(self):
        self.name = ''
        self.next_addr = 0
        self.addr = 0
        self.num_queue = 1  # HSMH中队列设置为4
        self.queues = [FifoQueue(1000)]
        # self.gcl = GCL()
        self.link= None #这边需要Link（）

    def enqueue(self, flow: Flow):
        self.queues[0].enqueue(flow)

    def dequeue(self, time: int) -> Optional[Flow]:
        for i in range(self.num_queue):
            if not self.queues[i].is_empty():
                return self.queues[i].dequeue()
        return None