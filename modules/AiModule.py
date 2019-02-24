# Copyright 2019 Xiang Li xiangl18@bu.edu
# AI Module

import random
import threading
import time


class AIModule(threading.Thread):
    """
    check the input type from the database in case there are some mistake data.
    """
    def __init__(self, queue, queue2):
        super().__init__()
        self.bo = []
        self.bp = []
        self.pulse = []
        self.queue = queue
        self.queue2 = queue2

    def run(self):
        """
        predict blood oxygen, blood pressure, pulse for each type from database.
        format:
        (float value)
        """
        time.sleep(3)
        try:
            for i, j, k in zip(self.queue.get(block=False), self.queue.get(block=False),
                               self.queue.get(block=False)):
                if (type(i) != float) or (type(j) != float) or (type(k) != float):
                    raise AttributeError
                else:
                    self.bo.append(i)
                    self.bp.append(j)
                    self.pulse.append(k)
        except AttributeError:
            print('input type false')
        rand = random.randint(1, len(self.bo))
        predBloodOxygen = 0
        predBloodPressure = 0
        prePulse = 0
        for i in range(rand):
            predBloodOxygen += self.bo[i]/rand
            predBloodPressure += self.bp[i]/rand
            prePulse += self.pulse[i]/rand
        # print('predicted blood oxygen is: ' + str(predBloodOxygen))
        # print('predicted blood pressure is: ' + str(predBloodPressure))
        # print('predicted pulse is: ' + str(prePulse))
        self.queue.put(self.bo, block=False)
        self.queue.put(self.bp, block=False)
        self.queue.put(self.pulse, block=False)
        self.queue2.put(predBloodOxygen, block=False)
        self.queue2.put(predBloodPressure, block=False)
        self.queue2.put(prePulse, block=False)

