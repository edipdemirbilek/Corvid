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

LIMIT = 1

args = sys.argv
sumo = SumoLogic(args[1], args[2])
fromTime = 1545091200000
toTime = 1545185976000
timeZone = "EST"
byReceiptTime = "false"

q = "_sourceCategory=qa/app/logs/api-schedule and LogMining: open_shift_requests \
| parse \"*  INFO\" as DateTime \
| parse \"LogMining: *,\" as operation \
| parse \"loggedInUser: *,\" as loggedInuser \
| parse \"companyId: *,\" as companyId \
| parse \"numberOfOpenShifts: *,\" as numberOfOpenShifts \
| parse \"approvalRequestIds: [*]\" as approvalRequestIds \
| where numberOfOpenShifts > 0 \
| sort by DateTime desc"

delay = 5
sj = sumo.search_job(q, fromTime, toTime, timeZone, byReceiptTime)

status = sumo.search_job_status(sj)
while status['state'] != 'DONE GATHERING RESULTS':
	if status['state'] == 'CANCELLED':
		break
	time.sleep(delay)
	status = sumo.search_job_status(sj)

print (status['state'])

if status['state'] == 'DONE GATHERING RESULTS':
    count = status['messageCount']
    limit = count if count < LIMIT and count != 0 else LIMIT # compensate bad limit check
    r = sumo.search_job_messages(sj, limit=limit)
    print (r)