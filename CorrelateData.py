#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:52:23 2018

@author: edip.demirbilek
"""
from util.TimeUtil import TimeUtil
from util.FileUtil import FileUtil


class CorrelateData:

    def run(sumologic_out_dir,
            sumologic_out_processed_dir,
            correlate_in_current_cycle_dir,
            correlate_in_previous_cycle_dir,
            correlate_in_processed_dir,
            correlate_out_dir):

        # move correlate in previous cycle to correlate in processed
        # move correlate in current cycle (Apply) to correlate in processed cycle
        # move correlate in current cycle (Requests) to correlate in previous cycle
        # copy sumologic out to correlate in current cycle
        # move sumologic out to sumologic out processed

        # correlate apply with requests in current and previoud cycle
        # write correlated data to correlate out dir with timestamp

        print("Not Implemented yet!")
