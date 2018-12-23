#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 21:55:18 2018

@author: edip.demirbilek
"""
from openshift.OpenShift import OpenShift


class OpenShiftApply(OpenShift):

    def __init__(self, accesId, accessKey):

        query = "_sourceCategory=qa/app/logs/api-schedule and LogMining: apply \
        | parse \"*  INFO\" as DateTime \
        | parse \"LogMining: *,\" as operation \
        | parse \"loggedInUser: *,\" as loggedInUser \
        | parse \"companyId: *,\" as companyId \
        | parse \"approvalRequestId: *,\" as approvalRequestId \
        | parse \"eventId: *,\" as eventId \
        | parse \"locationId: *\" as locationId \
        | sort by DateTime desc"

        super().__init__(accesId, accessKey, query)
