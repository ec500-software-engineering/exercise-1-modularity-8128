# URL: https://github.com/WenjieLuo2333/ModuleDesign/blob/master/InputModule_lxc.py
# Copyright 2019 Xiaocheng Liang xcliang@bu.edu
# Input Module

import threading


class InputModule(threading.Thread):
    """
    Since we do not have data from the sensor now, we assuse that data is already in txt file
    """
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def open(self, path):
        try:
            with open(path, 'r') as f:
                read = f.read().split()
        except Exception:
            print("Reading data error")

        if len(read) == 0:
            print("empty data")
        res = [float(i) for i in read]
        return res

    def run(self):
        pathbo = './example/examplebo.txt'
        pathbp = './example/examplebp.txt'
        pathpul = './example/examplepul.txt'
        bo = self.open(pathbo)
        bp = self.open(pathbp)
        pul = self.open(pathpul)
        self.queue.put(bo, block=False)
        self.queue.put(bp, block=False)
        self.queue.put(pul, block=False)






