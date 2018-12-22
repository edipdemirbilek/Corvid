#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 21:55:18 2018

@author: edip.demirbilek
"""
import json
import sys
import time

from sumologic.SumoLogic import SumoLogic

class OpenShiftRequests(object):

    def __init__(self, accesId, accessKey):
        self.sumo = SumoLogic(accesId, accessKey)

        self.q = "_sourceCategory=qa/app/logs/api-schedule and LogMining: open_shift_requests \
        | parse \"*  INFO\" as DateTime \
        | parse \"LogMining: *,\" as operation \
        | parse \"loggedInUser: *,\" as loggedInuser \
        | parse \"companyId: *,\" as companyId \
        | parse \"numberOfOpenShifts: *,\" as numberOfOpenShifts \
        | parse \"approvalRequestIds: [*]\" as approvalRequestIds \
        | where numberOfOpenShifts > 0 \
        | sort by DateTime desc"

    def get(self, fromTime, toTime, limit=1, timeZone="EST", byReceiptTime="false"):

        LIMIT = limit

        delay = 5
        sj = self.sumo.search_job(self.q, fromTime, toTime, timeZone, byReceiptTime)

        status = self.sumo.search_job_status(sj)
        while status['state'] != 'DONE GATHERING RESULTS':
        	if status['state'] == 'CANCELLED':
        		break
        	time.sleep(delay)
        	status = self.sumo.search_job_status(sj)

        print (status['state'])

        if status['state'] == 'DONE GATHERING RESULTS':
            count = status['messageCount']
            limit = count if count < LIMIT and count != 0 else LIMIT # compensate bad limit check
            r = self.sumo.search_job_messages(sj, limit=limit)
            print (r)



