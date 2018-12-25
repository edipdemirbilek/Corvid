#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:52:23 2018

@author: edip.demirbilek
"""
import json
import requests
import pprint

from util.TimeUtil import TimeUtil
from util.FileUtil import FileUtil
from util.RestUtil import RestUtil


class EnrichData:

    def run(env, username, password, correlate_data_params, enrich_data_params):

        correlate_out_dir = correlate_data_params["correlate_out_dir"]
        correlate_out_archive_dir = correlate_data_params["correlate_out_archive_dir"]
        enrich_in_dir = enrich_data_params["enrich_in_dir"]
        enrich_in_archive_dir = enrich_data_params["enrich_in_archive_dir"]
        enrich_out_dir = enrich_data_params["enrich_out_dir"]

        # move enrich in to enrich in processed
        # copy correlate data out to enrich in
        # move correlate out to correlate out processed

        # Authenticate
        xtoken = RestUtil.authenticate(env, username, password)
        print("xtoken: {}".format(xtoken))

        # Get Info for the User in context
        # Get Info for the Event in context

        # write enriche data to out dir with timestamp


