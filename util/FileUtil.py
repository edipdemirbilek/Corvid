#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 20:23:21 2018

@author: edip.demirbilek
"""
from pathlib import Path

class FileUtil(object):

    def read_timestamp_or_deafult(self, filename, past_time):
        config = Path(filename)

        if config.is_file():
            with open(filename, 'r') as fp:
                timestamp = fp.readline()

                if timestamp:
                    return timestamp

        return past_time
