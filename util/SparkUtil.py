#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 20:23:21 2018

@author: edip.demirbilek
"""
from pathlib import Path
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession


class SparkUtil():

    def get_df_from_csv_dirs(dir1, dir2, file_name_filter):
        sc = SparkContext.getOrCreate()
        spark = SparkSession(sc)
        df = spark.read.format("csv").option("header", "true").option("inferSchema", 'true').option('mode', 'FAILFAST').csv([dir1+file_name_filter, dir2+file_name_filter])
        return df

    def get_df_from_csv_dir(dir1, file_name_filter):
        sc = SparkContext.getOrCreate()
        spark = SparkSession(sc)
        df = spark.read.format("csv").option("header", "true").option("inferSchema", 'true').option('mode', 'FAILFAST').csv(dir1+file_name_filter)
        return df
