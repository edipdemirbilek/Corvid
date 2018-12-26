#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 14:16:04 2018

@author: edip.demirbilek
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:52:23 2018

@author: edip.demirbilek
"""
from util.TimeUtil import TimeUtil
from util.FileUtil import FileUtil


class UpdateDataset:

    def run(enrich_data_params, update_dataset_params):

        enrich_out_dir = enrich_data_params["enrich_out_dir"]
        enrich_out_archive_dir = enrich_data_params["enrich_out_archive_dir"]
        update_in_dir = update_dataset_params["update_in_dir"]
        update_in_archive_dir = update_dataset_params["update_in_archive_dir"]
        update_out_dir = update_dataset_params["update_out_dir"]

        # move update in to update processed
        # copy enrich out data to update in dir
        # move enrich out to enrich out processed
        # update dataset
        # write to update out dir with timestamp

        print("Not Implemented yet!")
