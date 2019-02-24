# URL: https://github.com/WenjieLuo2333/ModuleDesign/blob/master/Alert_module.py
# Copyright 2019 Wenjie Luo wjluo@bu.edu
# Alert Module

# It's the I/O documentation for Alert System

# Alert Sys
import numpy
import threading
import time


class Alert(threading.Thread):
    def __init__(self, queue, queue2):
        super().__init__()
        self.bo = []
        self.bp = []
        self.pul = []
        self.boi = []
        self.bpi = []
        self.puli = []
        self.queue = queue
        self.queue2 = queue2
        self.average_list = [[] for i in range(3)]
        self.alert_flag = -1
        self.dic = {0: 'Blood Oxygen', 1: 'Blood Pressure', 2: 'Pulse'}

    def exceed_threshold(self, data, tp):
        if tp == 0:
            if not 0.1 <= data <= 0.3:
                return 0
            else:
                return -1
        elif tp == 1:
            if not 80 <= data <= 120:
                return 1
            else:
                return -1
        else:
            if not 60 <= data <= 90:
                return 2
            else:
                return -1

    def Alert_Output(self):
        """
        Compare data with certain threthold
        send flags to user interface module.
        """
        if self.alert_flag != -1:
            return self.alert_flag
        else:
            return -1

    def Alert_for_three_categories_input(self, data_in):
        """
        get data for each type from database.
        format:
            (double value,int type)
        """
        if len(self.average_list[data_in[1]]) < 20:
            self.average_list[data_in[1]].append(float(data_in[0]))
        else:
            del (self.average_list[data_in[1]][0])
            self.average_list[data_in[1]].append(float(data_in[0]))

        if len(self.average_list[0]) > 2 and self.exceed_threshold(numpy.mean(self.average_list[0]),'bo') != -1:
            self.alert_flag = self.exceed_threshold(numpy.mean(self.average_list[data_in[1]]),'bo')
        if len(self.average_list[1]) > 2 and self.exceed_threshold(numpy.mean(self.average_list[1]),'bp') != -1:
            self.alert_flag = self.exceed_threshold(numpy.mean(self.average_list[data_in[1]]),'bp')
        if len(self.average_list[2]) > 2 and self.exceed_threshold(numpy.mean(self.average_list[2]),'pul') != -1:
            self.alert_flag = self.exceed_threshold(numpy.mean(self.average_list[data_in[1]]),'pul')

    def run(self):
        time.sleep(3)
        self.bo = self.queue.get(block=False)
        self.bp = self.queue.get(block=False)
        self.pul = self.queue.get(block=False)
        for k in range(len(self.bo)):
            self.boi = self.bo[k], 0
            self.bpi = self.bp[k], 1
            self.puli = self.pul[k], 2
        for k in range(len(self.bo)):
            self.Alert_for_three_categories_input(self.boi)
            self.Alert_for_three_categories_input(self.bpi)
            self.Alert_for_three_categories_input(self.puli)
            alert = self.Alert_Output()
            if alert != -1:
                # print("Alert", self.dic[alert])
                self.queue2.put("Alert" + self.dic[alert], block=False)
            else:
                # print("All good.")
                self.queue2.put("All good.", block=False)
        self.queue.put(self.bo, block=False)
        self.queue.put(self.bp, block=False)
        self.queue.put(self.pul, block=False)

