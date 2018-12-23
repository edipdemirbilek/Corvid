#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:58:48 2018

@author: edip.demirbilek
"""
import time


class TimeUtil(object):

    def __init__(self):
        self.one_day_in_millis = 86400000

    def get_current_milli_time(self):
        return int(round(time.time() * 1000))

    def get_past_milli_time(self, num_days):
        return self.get_current_milli_time() \
                - (self.one_day_in_millis * num_days)
