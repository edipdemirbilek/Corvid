#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 12:45:13 2018

@author: edip.demirbilek
"""
import sys

from GetData import GetData
from CorrelateData import CorrelateData
from EnrichData import EnrichData
from UpdateDataset import UpdateDataset


args = sys.argv

print("\n############# STEP 1: GET DATA FROM SUMOLOGIC SERVER #############\n")
accesId = args[1]
accessKey = args[2]

get_data_params = {}
get_data_params["sumologic_timestamp_dir"] = 'data/sumologic/timestamp/'
get_data_params["sumologic_out_dir"] = 'data/sumologic/out/'
get_data_params["sumologic_out_archive_dir"] = 'data/sumologic/out/archive/'

GetData.run(accesId, accessKey, get_data_params, remove_timestamp_files=True)

print("\n############# STEP 2: CORRELATE DATA #############################\n")

correlate_data_params = {}
correlate_data_params["correlate_in_current_cycle_dir"] = 'data/corralete/in/current/'
correlate_data_params["correlate_in_previous_cycle_dir"] = 'data/corralete/in/previous/'
correlate_data_params["correlate_in_archive_dir"] = 'data/corralete/in/archive/'
correlate_data_params["correlate_out_dir"] = 'data/corralete/out/'
correlate_data_params["correlate_out_archive_dir"] = 'data/corralete/out/archive/'

CorrelateData.run(get_data_params, correlate_data_params)

print("\n############# STEP 3: ENRICH DATA ################################\n")

enrich_data_params = {}
enrich_data_params["enrich_in_dir"] = 'data/enrich/in/'
enrich_data_params["enrich_in_archive_dir"] = 'data/enrich/in/archive/'
enrich_data_params["enrich_out_dir"] = 'data/enrich/out'
enrich_data_params["enrich_out_archive_dir"] = 'data/enrich/out/archive/'

EnrichData.run(correlate_data_params, enrich_data_params)

print("\n############# STEP 4: UPDATE DATASET #############################\n")

enrich_dataset_params = {}
enrich_dataset_params["update_in_dir"] = 'data/update/in/'
enrich_dataset_params["update_in_archive_dir"] = 'data/update/in/archive/'
enrich_dataset_params["update_out_dir"] = 'data/update/out/'

UpdateDataset.run(enrich_data_params, enrich_dataset_params)
