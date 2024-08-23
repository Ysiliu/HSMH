#!/usr/bin/env python3
# *-* coding:utf8 *-*


from component.flow import Flow,FlowType
from component.fifoqueue import FifoQueue
from component.heapqueue import EDFHeapQueue,STFHeapQueue
from config.config import ThresholdValue
from component.gcl import GCL
from typing import Optional
from component.link import Link


class Port:
    def __init__(self,name:str,addr:int,next_addr:int,gcl,link):
        self.name = name
        self.next_addr = next_addr
        self.addr = addr
        self.num_queue = 4
        self.queues = [EDFHeapQueue(1000), EDFHeapQueue(1000),FifoQueue(1000), STFHeapQueue(1000)]
        self.gcl = gcl
        self.link = link
        self.in_queue=FifoQueue(1000)
        self.thresholdvalue = ThresholdValue

    def enqueue(self, flow: Flow):
        if flow.type == FlowType.avb_a:
            self.queues[0].enqueue(flow)
        elif flow.type == FlowType.avb_b:
            self.queues[1].enqueue(flow)
        elif flow.type == FlowType.be:
            if flow.size <=  self.thresholdvalue:
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
    def __init__(self,name:str,addr:int,next_addr:int,link):
        self.name = name
        self.next_addr = next_addr
        self.addr = addr
        self.num_queue = 1
        self.queues = [FifoQueue(1000)]
        # self.gcl = GCL()
        self.link= link

    def enqueue(self, flow: Flow):
        self.queues[0].enqueue(flow)

    def dequeue(self, time: int) -> Optional[Flow]:
        for i in range(self.num_queue):
            if not self.queues[i].is_empty():
                return self.queues[i].dequeue()
        return None

class Port_siml_EDF:
    def __init__(self,name:str,addr:int,next_addr:int,gcl,link):
        self.name = name
        self.next_addr = next_addr
        self.addr = addr
        self.num_queue = 4
        self.queues = [EDFHeapQueue(1000), EDFHeapQueue(1000),FifoQueue(1000), STFHeapQueue(1000)]
        self.gcl = gcl
        self.link = link
        self.in_queue=FifoQueue(1000)
        self.thresholdvalue = ThresholdValue

    def enqueue(self, flow: Flow):
        if flow.type == FlowType.avb_a:
            self.queues[0].enqueue(flow)
        elif flow.type == FlowType.avb_b:
            self.queues[0].enqueue(flow)
        elif flow.type == FlowType.be:
            if flow.size <=  self.thresholdvalue:
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