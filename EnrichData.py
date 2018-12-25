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

    def run(debug, env, username, password, correlate_data_params, enrich_data_params):

        correlate_out_dir = correlate_data_params["correlate_out_dir"]
        correlate_out_archive_dir = correlate_data_params["correlate_out_archive_dir"]
        enrich_in_dir = enrich_data_params["enrich_in_dir"]
        enrich_in_archive_dir = enrich_data_params["enrich_in_archive_dir"]
        enrich_out_dir = enrich_data_params["enrich_out_dir"]

        # copy correlate data out to enrich in
        # move correlate out to correlate out archive
        FileUtil.copy_and_nove_files(correlate_out_dir,
                                     enrich_in_dir,
                                     correlate_out_archive_dir, "*.csv")

        # Authenticate
        print("\nAuthenticating user...")
        xtoken = RestUtil.authenticate(env, username, password)
        print("Authentication Sucessfull: X-Token: {}".format(xtoken))

        print("\nLoading Data to be enriched from Filesystem...")
        df_enrich = FileUtil.get_df_from_csv_dir(enrich_in_dir, "*.csv")
        print("Complete. Count: " + str(df_enrich.shape[0]))

        print("\nEnriching User and Event info...")
        for index, row in df_enrich.iterrows():
            loggedinuser = row['loggedinuser']
            companyid = row['companyid']
            query_datetime = row['query_datetime']
            apply_datetime = row['apply_datetime']
            numberofopenshifts = row['numberofopenshifts']
            locationid = row['locationid']
            eventid = row['eventid']
            applied = row['applied']

            # Get Info for the User in context
            response = RestUtil.get_user_details(debug, env, xtoken, companyid, loggedinuser)

            # Get Info for the Event in context
            response = RestUtil.get_event_details(debug, env, xtoken, companyid, locationid, eventid)

            # write enriche data to out dir with timestamp

        print("Complete. Count: {} \n".format(str(df_enrich.shape[0])))

        # move enrich in to enrich in archive
        FileUtil.move_files(enrich_in_dir,
                            enrich_in_archive_dir, "*.csv")