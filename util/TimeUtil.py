#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:58:48 2018

@author: edip.demirbilek
"""
import time


class TimeUtil():

    one_day_in_millis = 86400000

    def get_current_milli_time():
        return int(round(time.time() * 1000))

    def get_past_milli_time(num_days):
        return TimeUtil.get_current_milli_time() \
            - int(TimeUtil.one_day_in_millis * num_days)
