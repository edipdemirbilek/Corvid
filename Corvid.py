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
print("\n############# STEP 1: GET DATA FROM SUMOLOGIC SERVER #############\n")
accesId = args[1]
accessKey = args[2]

sumologic_data_out_dir = 'data/sumologic/out/'
sumologic_data_timestamp_dir = 'data/sumologic/timestamp/'
sumologic_data_processed_dir = 'data/sumologic/out/processed/'

GetData.run(accesId, accessKey,
            sumologic_data_out_dir, sumologic_data_timestamp_dir,
            remove_timestamp_files=True)

# step 2: Correlate Data
print("\n############# STEP 2: CORRELATE DATA #############################\n")

# Step 3: Enrich Data
print("\n############# STEP 2: ENRICH DATA ################################\n")
