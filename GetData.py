#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:52:23 2018

@author: edip.demirbilek
"""
from util.TimeUtil import TimeUtil
from util.FileUtil import FileUtil
from openshift.OpenShiftRequests import OpenShiftRequests
from openshift.OpenShiftApply import OpenShiftApply


class GetData:

    def run(accesId, accessKey, out_dir, timestamp_dir):

        # now in milliseconds
        now_timestamp = TimeUtil.get_current_milli_time()

        requests_timestamp_filename = 'OpenShiftRequests.timestamp'
        apply_timestamp_filename = 'OpenShiftApply.timestamp'

        requests_filename = 'OpenShiftRequests_'+str(now_timestamp)+".csv"
        apply_filename = 'OpenShiftApply_'+str(now_timestamp)+".csv"

        # temporary: remove files
        FileUtil.delete_if_exist(timestamp_dir+requests_timestamp_filename)
        FileUtil.delete_if_exist(timestamp_dir+apply_timestamp_filename)

        # fromTime for open shift requests
        past_requests_timestamp = FileUtil.read_timestamp_or_deafult(
                timestamp_dir+requests_timestamp_filename,
                TimeUtil.get_past_milli_time(3))

        # fromTime for open shift apply
        past_apply_timestamp = FileUtil.read_timestamp_or_deafult(
                timestamp_dir+apply_timestamp_filename,
                TimeUtil.get_past_milli_time(3))

        # get open shift requests and write to file
        open_shift_requests = OpenShiftRequests(accesId, accessKey)
        open_shift_requests.get_sumologic_content(
                past_requests_timestamp, now_timestamp, 1000)
        open_shift_requests.write_response_to_file(out_dir+requests_filename)

        # get open shift apply and write to file
        open_shift_apply = OpenShiftApply(accesId, accessKey)
        open_shift_apply.get_sumologic_content(
                past_apply_timestamp, now_timestamp, 1000)
        open_shift_apply.write_response_to_file(out_dir+apply_filename)

        # write timestamps
        FileUtil.write_timestamp(timestamp_dir+requests_timestamp_filename,
                                 now_timestamp)
        FileUtil.write_timestamp(timestamp_dir+apply_timestamp_filename,
                                 now_timestamp)
