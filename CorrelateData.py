#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:52:23 2018

@author: edip.demirbilek
"""
import csv
import re
from ast import literal_eval as make_tuple

from util.TimeUtil import TimeUtil
from util.FileUtil import FileUtil


class CorrelateData:

    def run(debug, get_data_params, correlate_data_params):

        sumologic_out_dir = get_data_params["sumologic_out_dir"]
        sumologic_out_archive_dir = get_data_params["sumologic_out_archive_dir"]
        correlate_in_current_cycle_dir = correlate_data_params["correlate_in_current_cycle_dir"]
        correlate_in_previous_cycle_dir = correlate_data_params["correlate_in_previous_cycle_dir"]
        correlate_in_archive_dir = correlate_data_params["correlate_in_archive_dir"]
        correlate_out_dir = correlate_data_params["correlate_out_dir"]

        # copy sumologic out to correlate in current cycle
        # move sumologic out to sumologic out archive
        FileUtil.copy_and_nove_files(sumologic_out_dir,
                                     correlate_in_current_cycle_dir,
                                     sumologic_out_archive_dir, "*.csv")

        # now in milliseconds
        now_timestamp = TimeUtil.get_current_milli_time()
        correlate_filename = 'Correlate_'+str(now_timestamp)+".csv"

        print("\nLoading Open Shift Requests from Filesystem...")
        # correlate apply with requests in current and previoud cycle
        df_requests = FileUtil.get_df_from_csv_dirs(correlate_in_current_cycle_dir,
                                                    correlate_in_previous_cycle_dir,
                                                    "Requests*")
        print("Complete. Count: " + str(df_requests.shape[0]))
        if(debug):
            for index, row in df_requests.iterrows():
                print(row)

        print("\nLoading Apply to Open Shifts from Filesystem...")
        df_apply = FileUtil.get_df_from_csv_dir(correlate_in_current_cycle_dir,
                                                    "Apply*")
        print("Complete. Count: " + str(df_apply.shape[0]))

        print("\nCorrelating Apply Open Shifts with Open Shifts Requests... ")

        fields = ['loggedinuser', 'companyid',
                  'query_datetime', 'apply_datetime', 'numberofopenshifts',
                  'locationid', 'eventid', 'applied']

        CorrelateData.add_header(correlate_out_dir+correlate_filename, fields)

        for index, row in df_apply.iterrows():

            apply_datetime = row['datetime']
            loggedinuser = row['loggedinuser']
            companyid = row['companyid']
            locationid = row['locationid']
            eventid = row['eventid']

            df_filtered = df_requests.loc[
                    (df_requests['loggedinuser'] == loggedinuser) &
                    (df_requests['companyid'] == companyid) &
                    (df_requests['datetime'] < apply_datetime) &
                    (df_requests['eventandlocationids'].str.contains(str(eventid)+","+str(locationid)))
                    ].drop_duplicates().sort_values(by=['datetime'], ascending=False).head(1)

            # lets first get rid of ', ' and replace it with '|' and then split
            # Example text: (3714cb1e-4839-4d8c-818e-9d01c655cd86,328038), (d87a2bb7-05e0-465e-8b6c-aa18d89a9c9f,328038), (e7bee5c5-8f4e-457f-95e7-b1ec82e8ab21,328038), (f04d14c1-68c3-4dda-8698-3d95eb3a4b9d,328038)
            events_and_locations = df_filtered.iloc[0]['eventandlocationids'].replace(', ','|').split('|')

            for event_location in events_and_locations:

                # lets get rid of paranthesis and split text by ','
                # Example text: (3714cb1e-4839-4d8c-818e-9d01c655cd86,328038)
                eventid_in_request, locationid_in_request = event_location.replace('(','').replace(')','').split(',')

                applied = False
                if str(eventid) == str(eventid_in_request) and str(locationid) == str(locationid_in_request):
                    applied = True

                row = {'loggedinuser': loggedinuser,
                       'companyid': companyid,
                       'query_datetime': df_filtered.iloc[0]['datetime'],
                       'apply_datetime': apply_datetime,
                       'numberofopenshifts': df_filtered.iloc[0]['numberofopenshifts'],
                       'locationid': locationid_in_request,
                       'eventid': eventid_in_request,
                       'applied': applied}

                CorrelateData.add_row(correlate_out_dir+correlate_filename, fields, row)

        print("Complete. Results written to: {} \n".format(correlate_out_dir+correlate_filename))

        # move correlate in previous cycle to correlate in archive
        FileUtil.move_files(correlate_in_previous_cycle_dir,
                            correlate_in_archive_dir, "*.csv")

        # move correlate in current cycle (Apply) to
        # correlate in archive cycle
        FileUtil.move_files(correlate_in_current_cycle_dir,
                            correlate_in_archive_dir, "Apply*")

        # move correlate in current cycle (Requests) to
        # correlate in previous cycle
        FileUtil.move_files(correlate_in_current_cycle_dir,
                            correlate_in_previous_cycle_dir, "Requests*")


    def add_header(filename, fields):
        with open(filename, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fields)
            writer.writeheader()

    def add_row(filename, fields, row):
        with open(filename, 'a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fields)
            writer.writerow(row)
