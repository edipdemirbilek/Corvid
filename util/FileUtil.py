#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 20:23:21 2018

@author: edip.demirbilek
"""
from pathlib import Path
import contextlib
import os
import glob
import shutil
import pandas as pd


class FileUtil():

    def read_timestamp_or_deafult(filename, past_time):
        config = Path(filename)

        if config.is_file():
            with open(filename, 'r') as fp:
                timestamp = fp.readline()

                if timestamp:
                    print("Read time stamp from file: {} value: {}".format(filename, str(timestamp)))
                    return timestamp

        print("No valid timestamp from file: {} Returning default value: {}".format(filename, str(past_time)))
        return past_time

    def delete_if_exist(filename):
        with contextlib.suppress(FileNotFoundError):
            os.remove(filename)

    def write_timestamp(filename, timestamp):
        with open(filename, 'w') as fp:
            print("Writing timestamp value: {} to file: {}". format(str(timestamp), filename))
            fp.write(str(timestamp))

    def move_files(src_dir, dst_dir, file_name_filter):
        print("Moving {} files from: {} to: {}".format(file_name_filter, src_dir, dst_dir))
        files = glob.iglob(os.path.join(src_dir, file_name_filter))
        for file in files:
            if os.path.isfile(file):
                shutil.move(file, dst_dir)

    def copy_files(src_dir, dst_dir, file_name_filter):
        print("Copying {} files from: {} to: {}".format(file_name_filter, src_dir, dst_dir))
        files = glob.iglob(os.path.join(src_dir, file_name_filter))
        for file in files:
            if os.path.isfile(file):
                shutil.copy(file, dst_dir)

    def copy_and_move_files(src_dir, dst_copy_dir, dst_move_dir, file_name_filter):
        print("Copying {} files from: {} to: {}".format(file_name_filter, src_dir, dst_copy_dir))
        print("Moving {} files from: {} to: {}".format(file_name_filter, src_dir, dst_move_dir))
        files = glob.iglob(os.path.join(src_dir, file_name_filter))
        for file in files:
            if os.path.isfile(file):
                shutil.copy(file, dst_copy_dir)
                shutil.move(file, dst_move_dir)

    def get_df_from_csv_dirs(dir1, dir2, file_name_filter):
        return pd.concat([FileUtil.get_df_from_csv_dir(dir1, file_name_filter),
                          FileUtil.get_df_from_csv_dir(dir1, file_name_filter)],
                    ignore_index=True)

    def get_df_from_csv_dir(dir1, file_name_filter):
        # glob.glob('data*.csv') - returns List[str]
        # pd.read_csv(f) - returns pd.DataFrame()
        # for f in glob.glob() - returns a List[DataFrames]
        # pd.concat() - returns one pd.DataFrame()
        return pd.concat([pd.read_csv(f) for f in glob.glob(dir1+file_name_filter)], ignore_index = True)

    def add_df_to_csv_file(df, filename):
        df.to_csv(filename, index=False)

    def write_to_file(filename, row):
        with open(filename, 'w') as file:
            #print(row)
            file.write(row)

    def file_exists(filename):
        if os.path.isfile(filename):
            return True
        return False

    def append_to_file(filename, row):
        with open(filename, 'a') as file:
            #print(row)
            file.write(row)
