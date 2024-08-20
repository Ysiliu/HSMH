#!/usr/bin/env python3
# *-* coding:utf8 *-*

"""
类别: 基本组件
名称: 任务类
作者: siliu
邮件: sj_jin@vip.hnist.edu.cn
日期: 2020年3月20日
说明: 重要的组件类
"""
from typing import List, Union, Any
import warnings
import pandas as pd


class NodeType(Enum):
    sw = 0
    es = 1

class Node(int):
    def __init__(self, id: int, type: NodeType) -> None:
        self.id = id
        self.type = type  
        self.sync_error = E_SYNC
        self.num_port = NUM_PORT
        self.queue_num = NUM_QUEUE

   
class GCL(list):
    """ 
    Args:
        init_list (): [link, queue, start, end, cycle]
    """

    def __init__(self, gcl_list: List[List]) -> None:
        if not gcl_list:
            raise ValueError("gcl_list cannot be empty")
        
        if not self.is_valid(gcl_list):
            raise ValueError("Invalid format: should be [link, queue, start, end, cycle]")

        self.format_gcl_type(gcl_list)
        self.check_overlap(gcl_list)
    

    @staticmethod
    def format_gcl_type(gcl_list: List[List]) -> None:
        """Convert GCL entries to appropriate types."""
        for i, row in enumerate(gcl_list):
            init_list[i] = [
                str(row[0]),
                int(row[1]),
                int(row[2]),
                int(row[3]),
                int(row[4]),
            ]

    @staticmethod
    def check_overlap(init_list: List[List[Union[str, int]]]) -> None:
        """Check if there is any overlap in GCL entries."""
        links = {row[0] for row in gcl_list}
        
        for link in links:
            gcl_for_link = sorted([row for row in init_list if row[0] == link], key=lambda x: x[2])
            for current, next_item in zip(gcl_for_link, gcl_for_link[1:]):
                if current[3] > next_item[2]:
                    warnings.warn(
                        f"Overlap detected in GCL: \n{current}\n{next_item}\n"
                    )

    @staticmethod
    def is_valid(gcl_list: List[List]) -> bool:
        """Validate the format of the GCL."""
        for item in gcl_list:
            if not isinstance(item[0], str):
                warnings.warn("Invalid link type in GCL")
                return False
            if len(item) != 5:
                return False
        return True

    def to_csv(self, path: str) -> None:
        """Export the GCL to a CSV file."""
        df = pd.DataFrame(self, columns=["link", "queue", "start", "end", "cycle"])
        df = df.sort_values(by=["link", "queue"])
        df.to_csv(path, index=False)            