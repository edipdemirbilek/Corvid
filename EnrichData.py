#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:52:23 2018

@author: edip.demirbilek
"""
from util.TimeUtil import TimeUtil
from util.FileUtil import FileUtil


class EnrichData:

    def run(correlate_data_params, enrich_data_params):

        correlate_out_dir = correlate_data_params["correlate_out_dir"]
        correlate_out_archive_dir = correlate_data_params["correlate_out_archive_dir"]
        enrich_in_dir = enrich_data_params["enrich_in_dir"]
        enrich_in_archive_dir = enrich_data_params["enrich_in_archive_dir"]
        enrich_out_dir = enrich_data_params["enrich_out_dir"]

        # move enrich in to enrich in processed
        # copy correlate data out to enrich in
        # move correlate out to correlate out processed
        # enrich data
        # write enriche data to out dir with timestamp

        print("Not Implemented yet!")
