#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:52:23 2018

@author: edip.demirbilek
"""
from util.TimeUtil import TimeUtil
from util.FileUtil import FileUtil
from service.WorkjamAPI import WorkjamAPI


class EnrichData:

    def run(debug, env, username, password, correlate_data_params, enrich_data_params):

        correlate_out_dir = correlate_data_params["correlate_out_dir"]
        correlate_out_archive_dir = correlate_data_params["correlate_out_archive_dir"]
        enrich_in_dir = enrich_data_params["enrich_in_dir"]
        enrich_in_archive_dir = enrich_data_params["enrich_in_archive_dir"]
        enrich_out_dir = enrich_data_params["enrich_out_dir"]

        # copy correlate data out to enrich in
        # move correlate out to correlate out archive
        FileUtil.copy_and_move_files(correlate_out_dir,
                                     enrich_in_dir,
                                     correlate_out_archive_dir, "*.csv")

        wj_api = WorkjamAPI(debug, env, username, password)

        # now in milliseconds
        now_timestamp = TimeUtil.get_current_milli_time()
        enrich_filename = 'Enrich_'+str(now_timestamp)+".csv"

        print("\nLoading Data to be enriched from Filesystem...")
        df_enrich = FileUtil.get_df_from_csv_dir(enrich_in_dir, "*.csv")
        print("Complete. Count: " + str(df_enrich.shape[0]))

        # write header to the file

        response_user_header = wj_api.get_user_details(True, '', '')
        response_event_header = wj_api.get_event_details(True, '', '', '')

        FileUtil.write_to_file(enrich_out_dir+enrich_filename,
                           'loggedin_user,company_id,query_datetime,apply_datetime,number_of_open_shifts,location_id,event_id,'
                                   + response_user_header + ','
                                   + response_event_header + ',applied\n')

        print("\nEnriching User and Event info...")

        num_records_written_to_file = 0

        for index, row in df_enrich.iterrows():
            loggedinuser = row['loggedinuser']
            companyid = row['companyid']
            query_datetime = row['query_datetime']
            apply_datetime = row['apply_datetime']
            numberofopenshifts = row['numberofopenshifts']
            locationid = row['locationid']
            eventid = row['eventid']
            applied = row['applied']

            try:
                # Get Info for the User in context
                response_user_csv = wj_api.get_user_details(False, companyid, loggedinuser)

                # Get Info for the Event in context
                response_event_csv = wj_api.get_event_details(False, companyid, locationid, eventid)

                # # write enriche data to out dir with timestamp
                FileUtil.append_to_file(enrich_out_dir+enrich_filename,
                                   str(loggedinuser) + ','
                                   + str(companyid) + ','
                                   + str(query_datetime) + ','
                                   + str(apply_datetime) + ','
                                   + str(numberofopenshifts) + ','
                                   + str(locationid) + ','
                                   + str(eventid) + ','
                                   + response_user_csv + ','
                                   + response_event_csv + ','
                                   + str(applied) + '\n')

                num_records_written_to_file += 1

            except Exception as e:
                # print(e)
                print(e)

        print("Complete. Found: {} Written: {}\n".format(str(df_enrich.shape[0]), num_records_written_to_file))

        # move enrich in to enrich in archive
        FileUtil.move_files(enrich_in_dir,
                            enrich_in_archive_dir, "*.csv")