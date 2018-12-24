#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 20:23:21 2018

@author: edip.demirbilek
"""
from pathlib import Path
import contextlib
import os
import glob, shutil
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession


class FileUtil():

    def read_timestamp_or_deafult(filename, past_time):
        config = Path(filename)

        if config.is_file():
            with open(filename, 'r') as fp:
                timestamp = fp.readline()

                if timestamp:
                    return timestamp

        return past_time

    def delete_if_exist(filename):
        with contextlib.suppress(FileNotFoundError):
            os.remove(filename)

    def write_timestamp(filename, timestamp):
        with open(filename, 'w') as fp:
            fp.write(str(timestamp))

    def move_files(src_dir, dst_dir, file_name_filter):
        files = glob.iglob(os.path.join(src_dir, file_name_filter))
        for file in files:
            if os.path.isfile(file):
                shutil.move(file, dst_dir)

    def copy_files(src_dir, dst_dir, file_name_filter):
        files = glob.iglob(os.path.join(src_dir, file_name_filter))
        for file in files:
            if os.path.isfile(file):
                shutil.copy(file, dst_dir)

    def copy_and_nove_files(src_dir, dst_copy_dir, dst_move_dir, file_name_filter):
        files = glob.iglob(os.path.join(src_dir, file_name_filter))
        for file in files:
            if os.path.isfile(file):
                shutil.copy(file, dst_copy_dir)
                shutil.move(file, dst_move_dir)
