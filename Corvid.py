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

sumologic_out_dir = 'data/sumologic/out/'
sumologic_timestamp_dir = 'data/sumologic/timestamp/'
sumologic_out_processed_dir = 'data/sumologic/out/processed/'

GetData.run(accesId, accessKey,
            sumologic_out_dir, sumologic_timestamp_dir,
            remove_timestamp_files=True)

print("\n############# STEP 2: CORRELATE DATA #############################\n")

correlate_in_current_cycle_dir = 'data/corralete/in/current/'
correlate_in_previous_cycle_dir = 'data/corralete/in/previous/'
correlate_in_processed_dir = 'data/corralete/in/processed/'
correlate_out_dir = 'data/corralete/out/'
correlate_out_processed_dir = 'data/corralete/out/processed/'

CorrelateData.run(sumologic_out_dir,
                  sumologic_out_processed_dir,
                  correlate_in_current_cycle_dir,
                  correlate_in_previous_cycle_dir,
                  correlate_in_processed_dir,
                  correlate_out_dir)

print("\n############# STEP 3: ENRICH DATA ################################\n")

enrich_in_dir = 'data/enrich/in/'
enrich_in_processed_dir = 'data/enrich/in/processed/'
enrich_out_dir = 'data/enrich/out'
enrich_out_processed_dir = 'data/enrich/out/processed/'

EnrichData.run(correlate_out_dir,
               correlate_out_processed_dir,
               enrich_in_dir,
               enrich_in_processed_dir,
               enrich_out_dir)

print("\n############# STEP 4: UPDATE DATASET #############################\n")

update_in_dir = 'data/update/in/'
update_in_processed_dir = 'data/update/in/processed/'
update_out_dir = 'data/update/out/'

UpdateDataset.run(enrich_out_dir,
                  enrich_out_processed_dir,
                  update_in_dir,
                  update_in_processed_dir,
                  update_out_dir)
