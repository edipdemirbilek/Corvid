#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 12:45:13 2018

@author: edip.demirbilek
"""
import sys

from GetData import GetData


args = sys.argv

# step 1: Get Data
accesId = args[1]
accessKey = args[2]

sumologic_data_out_dir = 'data/sumologic/out/'
sumologic_data_timestamp_dir = 'data/sumologic/timestamp/'
sumologic_data_processed_dir = 'data/sumologic/out/processed/'

GetData.run(accesId, accessKey,
            sumologic_data_out_dir, sumologic_data_timestamp_dir)

# step 2: Correlated Data

# Step 3: Enrich Data
