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

## Parameters 
T_SLOT = 100  ## Use 120 * 60 ns to apply on TTTech TSN board
T_PROC = 2000
T_M = int(1e16)
E_SYNC = 0
MAX_QUEUE_NUM = 8
PORT_NUM = 4

SEED = 1024
T_LIMIT = 120 * 60
M_LIMIT = 4096
DEBUG = False


class Release(list):
    """ [flow_id, release_time] """

    def __init__(self, rel_list: List[List[int]]) -> None:
        if rel_list:
            self.validate_and_initialize(rel_list)
        else:
            raise ValueError("Initialization list cannot be empty")

    def validate_and_initialize(self, rel_list: List[List[int]]) -> None:
        if self.is_valid(rel_list):
            self.format(gcl_list)
        else:
            raise ValueError("Invalid format: Each entry must be [flow_id, release_time]")

    @staticmethod
    def is_valid(init_list: List[List[int]]) -> bool:
        return all(len(item) == 2 for item in rel_list)

    @staticmethod
    def format(init_list: List[List[int]]) -> None:
    
        for i, row in enumerate(init_list):
            rel_list[i] = [int(val) for val in row]

    def to_csv(self, path: str) -> None:
        """ Exports the Release list to a CSV file. """
        result = pd.DataFrame(self)
        result.columns = ["stream","release_time"]
        result = result.sort_values(by=["stream", "frame"])
        result.to_csv(path, index=False)