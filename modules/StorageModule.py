# URL: https://github.com/WenjieLuo2333/ModuleDesign/blob/master/storage.py
# Copyright 2019 Gang Wei wg0502@bu.edu
# Storage Module
import threading
import time


class Storage(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.bo = []
        self.bp = []
        self.pul = []
        self.input = 0
        self.queue = queue

    def getIput(self, get):
        self.input = get

    def run(self):
        time.sleep(2)
        self.bo = self.queue.get(block=False)
        self.bp = self.queue.get(block=False)
        self.pul = self.queue.get(block=False)
        if self.input == "bo":
            print('current blood oxygen: {}'.format(self.bo))
        elif self.input == "bp":
            print('current blood pressure: {}'.format(self.bp))
        elif self.input == "pul":
            print('current pulse: {}'.format(self.pul))
        self.queue.put(self.bo, block=False)
        self.queue.put(self.bp, block=False)
        self.queue.put(self.pul, block=False)

