#!/usr/bin/env python3
# *-* coding:utf8 *-*



import heapq
from typing import List, Optional
from component.flow import Flow

class EDFHeapQueue:
    def __init__(self, num: int):
        self.num = num
        self.queue = []
        self.entry_count = 0

    def enqueue(self, flow: Flow):
        if len(self.queue) < self.num:
            heapq.heappush(self.queue, (flow.deadline, self.entry_count, flow))
            self.entry_count += 1
        else:
            print(f"Queue is full. Unable to enqueue Flow {flow.id}.")


    def dequeue(self) -> Optional[Flow]:
        if self.queue:
            _, _, flow = heapq.heappop(self.queue)
            return flow
        else:
            print("Queue is empty. Unable to dequeue.")
            return None

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def is_full(self) -> bool:
        return len(self.queue) == self.num

    def size(self) -> int:
        return len(self.queue)

    def clear(self) -> None:
        self.queue.clear()
        self.entry_count = 0

class STFHeapQueue:
    def __init__(self, num: int):
        self.num = num
        self.queue = []
        self.entry_count = 0

    def enqueue(self, flow: Flow):
        if len(self.queue) < self.num:
            heapq.heappush(self.queue, (flow.size, self.entry_count, flow))
            self.entry_count += 1
        else:
            print(f"Queue is full. Unable to enqueue Flow {flow.id}.")
            return False

    def dequeue(self) -> Optional[Flow]:
        if self.queue:
            _, _, flow = heapq.heappop(self.queue)
            return flow
        else:
            print("Queue is empty. Unable to dequeue.")
            return None

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def is_full(self) -> bool:
        return len(self.queue) == self.num

    def size(self) -> int:
        return len(self.queue)

    def clear(self) -> None:
        self.queue.clear()
        self.entry_count = 0