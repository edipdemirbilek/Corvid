#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:52:23 2018

@author: edip.demirbilek
"""
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession

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
        FileUtil.move_files(correlate_in_previous_cycle_dir,
                            correlate_in_processed_dir, "*.csv")

        # move correlate in current cycle (Apply) to
        # correlate in processed cycle
        FileUtil.move_files(correlate_in_current_cycle_dir,
                            correlate_in_processed_dir, "Apply*")

        # move correlate in current cycle (Requests) to
        # correlate in previous cycle
        FileUtil.move_files(correlate_in_current_cycle_dir,
                            correlate_in_previous_cycle_dir, "Requests*")

        # copy sumologic out to correlate in current cycle
        # move sumologic out to sumologic out processed
        FileUtil.copy_and_nove_files(sumologic_out_dir,
                                     correlate_in_current_cycle_dir,
                                     sumologic_out_processed_dir, "*.csv")

        # correlate apply with requests in current and previoud cycle
        df_requests = FileUtil.get_df_from_csv_dirs(correlate_in_current_cycle_dir,
                                                    correlate_in_previous_cycle_dir,
                                                    "Requests*")
#        print(df_requests.shape)
#        print(df_requests.head())


#        for index, row in df_requests.iterrows():
#            #print(row)
#            datetime = row['datetime']
#            loggedinuser = row['loggedinuser']
#            companyid = row['companyid']
#            numberofopenshifts = row['numberofopenshifts']
#            eventandlocationids = row['eventandlocationids']
#
#            if (numberofopenshifts > 1):
#                print("BINGO " + str(numberofopenshifts))

        df_apply = FileUtil.get_df_from_csv_dir(correlate_in_current_cycle_dir,
                                                    "Apply*")
#        print(df_apply.shape)
#        print(df_apply.head())

        for index, row in df_apply.iterrows():

            datetime = row['datetime']
            loggedinuser = row['loggedinuser']
            companyid = row['companyid']
            locationid = row['locationid']
            eventid = row['eventid']

            df_filtered = df_requests.loc[
                    (df_requests['loggedinuser'] == loggedinuser) &
                    (df_requests['companyid'] == companyid) &
                    (df_requests['datetime'] < datetime) &
                    (df_requests['eventandlocationids'].str.contains(str(eventid)+","+str(locationid)))
                    ].drop_duplicates().sort_values(by=['datetime'], ascending=False).head(1)

            #if (df_filtered.iloc[0]['numberofopenshifts'] > 1):
            print("\nloggedinuser: ", loggedinuser)
            print("companyid: ", companyid)
            print("datetime: ", datetime)
            print("locationid: ", locationid)
            print("eventid: ", eventid)
            print("numberofopenshifts: ", df_filtered.iloc[0]['numberofopenshifts'])
            print("eventandlocationids: ", df_filtered.iloc[0]['eventandlocationids'])


        # write correlated data to correlate out dir with timestamp
