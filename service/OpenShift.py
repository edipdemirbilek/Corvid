#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 21:55:18 2018

@author: edip.demirbilek
"""
import time

from sumologic.SumoLogic import SumoLogic


class OpenShift(object):

    open_shift_response = ''

    def __init__(self, accesId, accessKey, query):
        self.sumo = SumoLogic(accesId, accessKey)
        self.q = query

    def get_open_shift_response(self):
        return self.open_shift_response

    def get_sumologic_content(self, fromTime, toTime, limit=1, timeZone="EST",
                              byReceiptTime="false"):

        LIMIT = limit

        delay = 5
        sj = self.sumo.search_job(
                self.q, fromTime, toTime, timeZone, byReceiptTime)

        status = self.sumo.search_job_status(sj)
        while status['state'] != 'DONE GATHERING RESULTS':
            if status['state'] == 'CANCELLED':
                break

            time.sleep(delay)
            status = self.sumo.search_job_status(sj)

        # print(status['state'])

        if status['state'] == 'DONE GATHERING RESULTS':
            count = status['messageCount']
            # compensate bad limit check
            limit = count if count < LIMIT and count != 0 else LIMIT
            self.open_shift_response = \
                self.sumo.search_job_messages(sj, limit=limit)

            return self.open_shift_response
