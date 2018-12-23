#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 20:23:21 2018

@author: edip.demirbilek
"""
from pathlib import Path
import contextlib
import os


class FileUtil(object):

    def read_timestamp_or_deafult(self, filename, past_time):
        config = Path(filename)

        if config.is_file():
            with open(filename, 'r') as fp:
                timestamp = fp.readline()

                if timestamp:
                    return timestamp

        return past_time

    def delete_if_exist(self, filename):
        with contextlib.suppress(FileNotFoundError):
            os.remove(filename)

    def write_timestamp(self, filename, timestamp):
        with open(filename, 'w') as fp:
            fp.write(str(timestamp))
