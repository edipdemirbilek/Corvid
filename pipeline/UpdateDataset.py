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
        dataset_file = update_dataset_params["dataset_file"]

        # copy correlate data out to enrich in
        # move correlate out to correlate out archive
        FileUtil.copy_and_move_files(enrich_out_dir,
                                     update_in_dir,
                                     enrich_out_archive_dir, "*.csv")

        print("\nLoading Data to be added to Dataset from Filesystem...")
        df_update = FileUtil.get_df_from_csv_dir(update_in_dir, "*.csv")
        print("Complete. Count: " + str(df_update.shape[0]))

        # get header
        header = ','.join(df_update.columns) + '\n'
        # print(header)

        # add header if file does not exist
        if not FileUtil.file_exists(dataset_file):
            FileUtil.write_to_file(dataset_file, header)

        # append to file
        FileUtil.add_df_to_csv_file(df_update, dataset_file)

        # move enrich in to enrich in archive
        FileUtil.move_files(update_in_dir,
                            update_in_archive_dir, "*.csv")
