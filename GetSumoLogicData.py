#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:52:23 2018

@author: edip.demirbilek
"""
import sys

from util.TimeUtil import TimeUtil
from util.FileUtil import FileUtil
from openshift.OpenShiftRequests import OpenShiftRequests
from openshift.OpenShiftApply import OpenShiftApply

args = sys.argv

requests_timestamp_filename = 'OpenShiftRequests.timestamp'
apply_timestamp_filename = 'OpenShiftApply.timestamp'

time_util = TimeUtil()
file_util = FileUtil()

# temporary: remove files
file_util.delete_if_exist(requests_timestamp_filename)
file_util.delete_if_exist(apply_timestamp_filename)

# fromTime for open shift requests
past_requests_timestamp = file_util.read_timestamp_or_deafult(
        requests_timestamp_filename, time_util.get_past_milli_time(3))

# fromTime for open shift apply
past_apply_timestamp = file_util.read_timestamp_or_deafult(
        apply_timestamp_filename, time_util.get_past_milli_time(3))

# now in milliseconds
now_timestamp = time_util.get_current_milli_time()

# get open shift requests
openShiftRequests = OpenShiftRequests(args[1], args[2])
open_shift_requests_lines = openShiftRequests.get(
        past_requests_timestamp, now_timestamp, 10)
print(open_shift_requests_lines)

# get open shift apply
openShiftapply = OpenShiftApply(args[1], args[2])
open_shift_apply_lines = openShiftapply.get(
        past_apply_timestamp, now_timestamp, 10)
print(open_shift_apply_lines)

# write timestamps
file_util.write_timestamp(requests_timestamp_filename, now_timestamp)
file_util.write_timestamp(apply_timestamp_filename, now_timestamp)
