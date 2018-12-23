#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:52:23 2018

@author: edip.demirbilek
"""
from util.TimeUtil import *
from util.FileUtil import *
from OpenShiftRequests import *

args = sys.argv

filename = 'LastProcessedRecord.timestamp'

time_util = TimeUtil()
file_util = FileUtil()

past = file_util.read_timestamp_or_deafult(filename, time_util.get_past_milli_time(3))
now = time_util.get_current_milli_time()

openShiftRequests = OpenShiftRequests(args[1], args[2])

open_shift_lines = openShiftRequests.get(past, now, 10)

with open(filename, 'w') as fp:
   fp.write(str(now))