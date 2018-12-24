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
from util.SparkUtil import SparkUtil


class CorrelateData:

    def run(sumologic_out_dir,
            sumologic_out_processed_dir,
            correlate_in_current_cycle_dir,
            correlate_in_previous_cycle_dir,
            correlate_in_processed_dir,
            correlate_out_dir):

        sc = SparkContext.getOrCreate()
        spark = SparkSession(sc)

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
        df_requests = SparkUtil.get_df_from_csv_dirs(correlate_in_current_cycle_dir,
                                                    correlate_in_previous_cycle_dir,
                                                    "Requests*")
        # DataFrame[environment: string, operation: string, datetime: timestamp, loggedinuser: bigint, companyid: bigint, numberofopenshifts: int, eventandlocationids: string]

        #df_requests.createOrReplaceTempView("df_request_view")
        #sql_way = spark.sql("""
        #                  SELECT COUNT(*) FROM df_request_view
        #                  """)
        df_way = df_requests.count()
        print(df_way)
        # print(df_way.explain())

        df_apply = SparkUtil.get_df_from_csv_dir(correlate_in_current_cycle_dir,
                                                    "Apply*")
        # DataFrame[environment: string, operation: string, datetime: timestamp, loggedinuser: bigint, companyid: bigint, locationid: bigint, eventid: string]
        df_way = df_apply.count()
        print(df_way)

        # write correlated data to correlate out dir with timestamp
