#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 21:55:18 2018

@author: edip.demirbilek
"""
import csv

from openshift.OpenShift import OpenShift


class OpenShiftApply(OpenShift):

    def __init__(self, accesId, accessKey):

        query = "_sourceCategory=qa/app/logs/api-schedule and LogMining: apply \
        | parse \"*  INFO\" as DateTime \
        | parse \"LogMining: *,\" as operation \
        | parse \"loggedInUser: *,\" as loggedInUser \
        | parse \"companyId: *,\" as companyId \
        | parse \"eventId: *,\" as eventId \
        | parse \"locationId: *\" as locationId \
        | sort by DateTime desc"

        super().__init__(accesId, accessKey, query)

    def write_response_to_file(self, filename):

        open_shift_apply_lines = super().get_open_shift_response()
        messages = open_shift_apply_lines['messages']
        fields = ['environment', 'operation', 'datetime', 'loggedinuser',
                  'companyid', 'locationid', 'eventid']

        with open(filename, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fields)
            writer.writeheader()

            for m in messages:
                tmp = m['map']

                row = {'environment': tmp['environment'],
                       'operation': tmp['operation'],
                       'datetime': tmp['datetime'],
                       'loggedinuser': tmp['loggedinuser'],
                       'companyid': tmp['companyid'],
                       'locationid': tmp['locationid'],
                       'eventid': tmp['eventid']}

                writer.writerow(row)
