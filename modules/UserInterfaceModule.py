# Copyright 2019 Xiang Li xiangl18@bu.edu
# User Interface Module

# It's the I/O documentation for the User_Interface_system
# User Interface
import threading
import time


class UserInterface(threading.Thread):
    def __init__(self, queue, queue2, queue3):
        super().__init__()
        self.bo = []
        self.bp = []
        self.pul = []
        self.boalert = []
        self.bpalert = []
        self.pulalert = []
        self.prebo = 0
        self.prebp = 0
        self.prepul = 0
        self.queue = queue
        self.queue2 = queue2
        self.queue3 = queue3

    def display(self):
        print("-" * 60)
        print("patients'current blood oxygen:", self.bo)
        print("patients'current blood pressure:", self.bp)
        print("patients'current pulse:", self.pul)
        print("-"*60)
        print("patients'current blood oxygen alert:", self.boalert)
        print("patients'current blood pressure alert:", self.bpalert)
        print("patients'current pulse alert:", self.pulalert)
        print("-"*60)
        print("patients' predicted blood oxygen is:", self.prebo)
        print("patients' predicted blood oxygen is:", self.prebp)
        print("patients' predicted blood oxygen is:", self.prepul)

    def run(self):
                time.sleep(4)
                self.bo = self.queue.get(block=False)
                self.bp = self.queue.get(block=False)
                self.pul = self.queue.get(block=False)
                self.boalert = self.queue2.get(block=False)
                self.bpalert = self.queue2.get(block=False)
                self.pulalert = self.queue2.get(block=False)
                self.prebo = self.queue3.get(block=False)
                self.prebp = self.queue3.get(block=False)
                self.prepul = self.queue3.get(block=False)
                self.display()



