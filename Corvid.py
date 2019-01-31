#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 12:45:13 2018

@author: edip.demirbilek
"""
import sys

from pipeline.GetData import GetData
from pipeline.CorrelateData import CorrelateData
from pipeline.EnrichData import EnrichData
from pipeline.UpdateDataset import UpdateDataset


args = sys.argv
acces_id = args[1]
access_key = args[2]
env = args[3]
username = args[4]
password = args[5]

num_days = 2
debug = False

print("\n############# STEP 1: GET DATA FROM SUMOLOGIC SERVER #############\n")

get_data_params = {}
get_data_params["sumologic_timestamp_dir"] = 'data/sumologic/timestamp/'
get_data_params["sumologic_out_dir"] = 'data/sumologic/out/'
get_data_params["sumologic_out_archive_dir"] = 'data/sumologic/out/archive/'

GetData.run(num_days, acces_id, access_key, env, get_data_params, remove_timestamp_files=False)

print("\n############# STEP 2: CORRELATE DATA #############################\n")

correlate_data_params = {}
correlate_data_params["correlate_in_current_cycle_dir"] = 'data/corralete/in/current/'
correlate_data_params["correlate_in_previous_cycle_dir"] = 'data/corralete/in/previous/'
correlate_data_params["correlate_in_archive_dir"] = 'data/corralete/in/archive/'
correlate_data_params["correlate_out_dir"] = 'data/corralete/out/'
correlate_data_params["correlate_out_archive_dir"] = 'data/corralete/out/archive/'

debug = False
CorrelateData.run(debug, get_data_params, correlate_data_params)

print("\n############# STEP 3: ENRICH DATA ################################\n")

enrich_data_params = {}
enrich_data_params["enrich_in_dir"] = 'data/enrich/in/'
enrich_data_params["enrich_in_archive_dir"] = 'data/enrich/in/archive/'
enrich_data_params["enrich_out_dir"] = 'data/enrich/out/'
enrich_data_params["enrich_out_archive_dir"] = 'data/enrich/out/archive/'

debug = False
EnrichData.run(debug, env, username, password, correlate_data_params, enrich_data_params)

print("\n############# STEP 4: UPDATE DATASET #############################\n")

update_dataset_params = {}
update_dataset_params["update_in_dir"] = 'data/update/in/'
update_dataset_params["update_in_archive_dir"] = 'data/update/in/archive/'
update_dataset_params["dataset_file"] = 'data/update/out/Dataset.csv'

UpdateDataset.run(enrich_data_params, update_dataset_params)
