#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:52:23 2018

@author: edip.demirbilek
"""
from util.TimeUtil import *
from OpenShiftRequests import *

args = sys.argv

time_util = TimeUtil()

openShiftRequests = OpenShiftRequests(args[1], args[2])

with open('LastProcessedRecord.timestamp', 'w') as fp:
   fp.write(str(time_util.get_past_milli_time(3)))

with open('LastProcessedRecord.timestamp', 'r') as fp:
   lastProcessedRecoredTimeStamp = fp.readline()
   openShiftRequests.get(lastProcessedRecoredTimeStamp, time_util.get_current_milli_time(), 10)