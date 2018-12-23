#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 21:55:18 2018

@author: edip.demirbilek
"""
from openshift.OpenShift import OpenShift


class OpenShiftRequests(OpenShift):

    def __init__(self, accesId, accessKey):
        query = "_sourceCategory=qa/app/logs/api-schedule and LogMining: open_shift_requests \
        | parse \"*  INFO\" as DateTime \
        | parse \"LogMining: *,\" as operation \
        | parse \"loggedInUser: *,\" as loggedInuser \
        | parse \"companyId: *,\" as companyId \
        | parse \"numberOfOpenShifts: *,\" as numberOfOpenShifts \
        | parse \"approvalRequestIds: [*]\" as approvalRequestIds \
        | where numberOfOpenShifts > 0 \
        | sort by DateTime desc"

        super().__init__(accesId, accessKey, query)

#    def get(self, fromTime, toTime, limit=1, timeZone="EST",
#            byReceiptTime="false"):
#
#        return super().get(fromTime, toTime, limit, timeZone, byReceiptTime)
