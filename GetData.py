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

    def run(accesId, accessKey, env, get_data_params, remove_timestamp_files=False):

        sumologic_timestamp_dir = get_data_params["sumologic_timestamp_dir"]
        sumologic_out_dir = get_data_params["sumologic_out_dir"]

        # now in milliseconds
        now_timestamp = TimeUtil.get_current_milli_time()

        requests_timestamp_filename = 'Requests.timestamp'
        apply_timestamp_filename = 'Apply.timestamp'

        requests_filename = 'Requests_'+str(now_timestamp)+".csv"
        apply_filename = 'Apply_'+str(now_timestamp)+".csv"

        # temporary: remove files
        if remove_timestamp_files:
            FileUtil.delete_if_exist(
                    sumologic_timestamp_dir+requests_timestamp_filename)
            FileUtil.delete_if_exist(
                    sumologic_timestamp_dir+apply_timestamp_filename)

        # fromTime for open shift requests
        past_requests_timestamp = FileUtil.read_timestamp_or_deafult(
                sumologic_timestamp_dir+requests_timestamp_filename,
                TimeUtil.get_past_milli_time(5))

        # fromTime for open shift apply
        past_apply_timestamp = FileUtil.read_timestamp_or_deafult(
                sumologic_timestamp_dir+apply_timestamp_filename,
                TimeUtil.get_past_milli_time(5))

        # get open shift requests and write to file
        print("Downloading Open Shift Requests from SumoLogic...")
        open_shift_requests = OpenShiftRequests(accesId, accessKey)
        open_shift_requests.get_sumologic_content(
                past_requests_timestamp, now_timestamp, 10000)

        open_shift_requests.write_response_to_file(
                sumologic_out_dir+requests_filename)
        print("Complete. Results written to "+sumologic_out_dir+requests_filename)

        # get open shift apply and write to file
        print("\nDownloading Apply to Open Shifts from SumoLogic...")
        open_shift_apply = OpenShiftApply(accesId, accessKey)
        open_shift_apply.get_sumologic_content(
                past_apply_timestamp, now_timestamp, 10000)

        open_shift_apply.write_response_to_file(
                sumologic_out_dir+apply_filename)
        print("Complete. Results written to "+sumologic_out_dir+apply_filename)

        # write timestamps
        FileUtil.write_timestamp(
                sumologic_timestamp_dir+requests_timestamp_filename,
                now_timestamp)
        FileUtil.write_timestamp(
                sumologic_timestamp_dir+apply_timestamp_filename,
                now_timestamp)
        print("\nUpdated time stamp files.")
