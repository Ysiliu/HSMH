#!/usr/bin/env python3
# *-* coding:utf8 *-*


from collections import deque
from typing import Optional
from component.flow import Flow

class FifoQueue:
    def __init__(self, num: int):
        self.num = num
        self.queue = deque(maxlen=num)

    def enqueue(self, flow: Flow):
        if len(self.queue) < self.num:
            self.queue.append(flow)
        else:
            print(f"Queue is full. Unable to enqueue Flow {flow.id}.")

    def dequeue(self) -> Optional[Flow]:
        if self.queue:
            return self.queue.popleft()
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