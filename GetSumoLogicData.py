#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:52:23 2018

@author: edip.demirbilek
"""
from util import *
from OpenShiftRequests import *

args = sys.argv

openShiftRequests = OpenShiftRequests(args[1], args[2])
openShiftRequests.get(1545091200000, 1545185976000)

lastProcessedRecoredTimeStamp = open('LastProcessedRecord.timestamp', 'a')

now = TimeUtil.current_milli_time()

print(now)
print(1545091200000)