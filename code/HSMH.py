"""
类别: 算法
名称: HSMH
作者: Ysiliu
邮件: sj_jin@vip.hnist.edu.cn
日期: 2023年6月26日
说明:
"""

import heapq
import matplotlib.pyplot as plt
import numpy as np
import openpyxl
import random
import sys

class FlowGenerator:
    def __init__(self, num_avb, num_be):
        self.num_avb = num_avb
        self.num_be = num_be
        self.flows = []

    def generate_flows(self):
        Type = ['AVB_B', 'AVB_A', 'BE']
        circle = [1200, 2400]
        self.flows = []

        for _ in range(self.num_avb):  # 生成AVB数据
            t = random.randint(0, 360)
            item = (t + random.randint(500, 8400), t, Type[random.randint(0, 1)], random.randint(5, 120),
                    circle[random.randint(0, 1)])  # 截止日期, 到达时间, 流的类型, 流的大小, 周期
            self.flows.append(item)

        for _ in range(self.num_be):  # 生成BE数据
            t = random.randint(0, 960)
            item = (random.randint(5, 120), t, Type[2], circle[random.randint(0, 1)])  # 流的大小, 到达时间, 流的类型, 周期
            self.flows.append(item)

    def save_flows(self, filename):
        with open(filename, "a") as file:
            file.write(str(self.flows) + "\n")


class FlowProcessor:
    def __init__(self, flows, tv):
        self.flows = flows
        self.qa = []
        self.qb = []
        self.qe = []
        self.qee = []
        self.cnt = 0
        self.link = -1
        self.linktime = 0
        self.idletime = 0
        self.ca = 0
        self.cb = 0
        self.ida = 560
        self.idb = 400
        self.sea = 240
        self.seb = 400
        self.gateab = 0
        self.gatee = 1
        self.avblimit = 0
        self.sendavb = 0
        self.sendbe = 0
        self.cntqa = 0
        self.cntqb = 0
        self.tv = tv
    def process_flows(self, tv):  #tv表示分流阈值
        i = 0
        while i <= 24000:
            self._check_time(i)
            self._flow_in(i, tv)
            self._flow_out(i)
            if self.link <= i and i % 1200 >= 360:
                if len(self.qa) > 0:
                    self.ca += self.ida
                if len(self.qb) > 0:
                    self.cb += self.idb
                if 1080 <= i % 1200 < 1200:
                    self.idletime += 1
            i += 1
        return self.idletime

    def _check_time(self, i):
        if i % 1200 < 360:
            self.gateab = 0
            self.gatee = 0
        elif 360 <= i % 1200 < 960:
            self.gateab = 1
            self.gatee = 1
        elif 960 <= i % 1200 < 1080:
            self.gateab = 0
            self.gatee = 1
        elif 1080 <= i % 1200 < 1200:
            self.gateab = 1
            self.gatee = 1

    def _flow_in(self, t, tv):
        while self.cnt < len(self.flows):
            flow = self.flows[self.cnt]
            if flow[1] <= t:
                if flow[2] == 'AVB_A':
                    heapq.heappush(self.qa, flow)
                elif flow[2] == 'AVB_B':
                    heapq.heappush(self.qb, flow)
                elif flow[2] == 'BE' and flow[0] <= tv:
                    heapq.heappush(self.qe, flow)
                else:
                    self.qee.append(flow)
                self.cnt += 1
            else:
                break

    def _flow_out(self, i):
        t = i % 1200
        if 360 <= t < 840:
            self._handle_avb(i, t)
        elif 840 <= t < 1080:
            self._handle_be(i, t)
        elif 1080 <= t < 1200:
            self._handle_avb(i, t)

    def _handle_avb(self, i, t):
        if len(self.qa) > 0 and self.ca >= 0 and self.link <= i and t + self.qa[0][3] < 1200:
            self._send_flow(i, self.qa, self.sea, self.idb,1)
        elif len(self.qb) > 0 and self.cb >= 0 and self.link <= i and t + self.qb[0][3] < 1200:
            self._send_flow(i, self.qb, self.seb, self.ida,2)
        elif len(self.qee) > 0 and self.link <= i and t + self.qee[0][0] < 1200:
            self._send_flow_from_queue(i, self.qee, self.ida, self.idb)
        elif len(self.qe) > 0 and self.link <= i and t + self.qe[0][0] < 1200:
            self._send_flow_from_queue(i, self.qe, self.ida, self.idb)

    def _handle_be(self, i, t):
        if len(self.qee) > 0 and self.link <= i and t + self.qee[0][0] < 1200:
            self._send_flow_from_queue(i, self.qee, self.ida, self.idb)
        elif len(self.qe) > 0 and self.link <= i and t + self.qe[0][0] < 1200:
            self._send_flow_from_queue(i, self.qe, self.ida, self.idb)

    def _send_flow(self, i, queue, se, id, flag):
        self.link = i + queue[0][3]
        if flag==1:
            self.ca -= queue[0][3] * se
            self.cb += queue[0][3] * id
        elif flag==2:
            self.cb -= queue[0][3] * se
            self.ca += queue[0][3] * id
        # self._show_flow(queue,i)    #打印输出流
        heapq.heappop(queue)

    def _send_flow_from_queue(self, i, queue, ida, idb):
        self.link = i + queue[0][0]
        self.ca += queue[0][0] * ida
        self.cb += queue[0][0] * idb
        # self._show_flow(queue,i)  #打印输出流
        queue.pop(0)

    # def _show_flow(self, queue,i):
    #     flow = queue[0]
    #     print(f'{i}--{i + flow[0]}---{flow}')
    #     self.linktime += flow[0]
    #     if flow[2] == 'BE':
    #         self.sendbe += 1
    #     else:
    #         self.sendavb += 1
    #         if flow[2] == 'AVB_A':
    #             self.cntqa += 1
    #         else:
    #             self.cntqb += 1
    #         if flow[0] >= i + flow[3]:
    #             self.avblimit += 1
    #         print(self.avblimit)


class FlowSimulation:
    def __init__(self, num_avb, num_be,tv):
        self.num_avb = num_avb
        self.num_be = num_be
        self.tv =tv

    def run(self):
        fg = FlowGenerator(self.num_avb, self.num_be)
        fg.generate_flows()
        flows = fg.flows
        fp = FlowProcessor(flows, self.tv)

        flows.sort(key=lambda x: int(x[1]))
        idletime = fp.process_flows(self.tv)


        #这边的分母需要根据流的数量进行计算
        # print(f'Idle Time: {idletime}')
        # print(f'Remain AVB_A: {len(fp.qa)},  AVB_B: {len(fp.qb)}')
        # print(f'Sent AVB: {fp.sendavb}')
        # print(f'AVB Limit: {fp.avblimit}')
        # print(f'AVB Send Rate: {fp.sendavb / 200}')
        # print(f'AVB Accept Rate: {fp.avblimit / 200}')
        # print(f'BE Send Rate: {fp.sendbe / 150}')
        # print(f'Link Time: {fp.linktime / 16800}')
        # print(f'HSMH = [{fp.sendavb / 200}, {fp.avblimit / 200}, {fp.sendbe / 150}, {fp.linktime / 16800}]')
        # print(f'cntqa: {fp.cntqa},  cntqb: {fp.cntqb}')


if __name__ == "__main__":
    fs=FlowSimulation(70 ,70,30)
    fs.run()