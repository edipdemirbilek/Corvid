#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 20:23:21 2018

@author: edip.demirbilek
"""
import pprint

from util.RestUtil import RestUtil


class WorkjamAPI(object):

    debug = False
    env = 'prod'
    username = ''
    password = ''
    xtoken = ''

    def __init__(self, debug, env, username, password):
        self.debug = debug
        self.env = env
        self.username = username
        self.password = password

    def get_base_url(self):
        if self.env == "qa":
            return "https://qa-api.workjamnp.com"

        return "https://api.workjam.com"

    def get_authentication_url(self):
        return self.get_base_url() + "/auth/v3"

    def get_authentication_data(self):
        return {"username": self.username,
                "password": self.password}

    def authenticate(self):
        url = self.get_authentication_url()
        data = self.get_authentication_data()

        response = RestUtil.post(url, data)
        # pprint.pprint(response.json())

        if response.status_code != 200:
            pprint.pprint(response.json())
            raise RuntimeError('Authentiction failed: {}'
                               .format(response.status_code))

        return self.get_xtoken(response)

    def get_event_url(self, companyid, locationid, eventid):
        return self.get_base_url() + "/api/v4/companies/{}/locations/{}/shifts/{}".format(str(companyid), str(locationid), str(eventid))

    def get_event_header_csv(self):
        return ""

    def event_dto_to_csv(self, event_dto):
#    #################### EVENT START #########################
#    {'allowedActions': ['DIRECT_SWAP', ],
#     'approvalRequests': [],
#     'assignees': [{'bookingMethod': 'ASSIGN',
#                    'breaks': [],
#                    'profile': {'firstName': 'And',
#                                'id': '370129',
#                                'lastName': 'Go'},
#                    'status': 'CONFIRMED'}],
#     'createdBy': {'id': '328237'},
#     'event': {'endDateTime': '2018-12-27T14:00:00.000+0000',
#               'id': '6171fbc7-dc57-42f8-9169-26f6459523e6',
#               'location': {'externalCode': '783336',
#                            'externalId': '783336',
#                            'id': '328038',
#                            'name': 'Lexington Rombus',
#                            'timeZoneId': 'America/Toronto',
#                            'type': 'STORE'},
#               'note': None,
#               'recurrence': None,
#               'startDateTime': '2018-12-27T13:00:00.000+0000',
#               'title': 'Employee EN',
#               'type': 'SHIFT'},
#     'externalFields': {'workjam': {'locationExternalCodesMap': {'328038': [None,
#                                                                            None,
#                                                                            None,
#                                                                            '783336']}}},
#     'externalId': '6171fbc7-dc57-42f8-9169-26f6459523e6',
#     'id': '6171fbc7-dc57-42f8-9169-26f6459523e6',
#     'locked': False,
#     'offeredSpots': {'remainingQuantity': 0},
#     'openSpots': {'broadcast': False,
#                   'remainingQuantity': 0,
#                   'requiresApproval': False,
#                   'useMarketplace': False,
#                   'useSeniorityList': False},
#     'position': {'externalId': '123', 'id': '393589', 'name': 'Employee EN'},
#     'quantity': 1,
#     'segments': [{'endDateTime': '2018-12-27T14:00:00.000+0000',
#                   'location': {'id': '328038',
#                                'name': 'Lexington Rombus',
#                                'timeZoneId': 'America/Toronto'},
#                   'position': {'id': '393589', 'name': 'Employee EN'},
#                   'startDateTime': '2018-12-27T13:00:00.000+0000',
#                   'type': 'SHIFT'}],
#     'status': 'PUBLISHED'}
    ##################### EVENT END ##########################

        return event_dto['createdBy']

    def get_event_details(self, companyid, locationid, eventid):
        url = self.get_event_url(companyid, locationid, eventid)

        if self.debug:
            print("URL: " + url)

        response = RestUtil.get(url, headers={"X-Token": self.xtoken})

        if(self.debug):
            print("#################### EVENT START #########################")
            pprint.pprint(response.json())
            print("##################### EVENT END ##########################")

        if response.status_code == 500:
            pprint.pprint(response.json())
            raise RuntimeError('Retrieving Event Details failed: {}'
                               .format(response.status_code))

        return self.event_dto_to_csv(response.json())

    def get_xtoken(self, response):
        return response.json()['token']

    def get_user_url(self, companyid, userid):
            return self.get_base_url() + "/api/v4/companies/{}/employees/{}".format(str(companyid), str(userid))

    def get_user_header_csv(self):
        return ""

    def user_dto_to_csv(self, event_json):
#    ##################### USER START #########################
#    {'badgeLevelIds': [543752,
#                       821517],
#     'birthDate': '2017-06-14',
#     'currentEmployments': [{'id': '370130',
#                             'location': {'externalCode': '783336',
#                                          'id': '328038',
#                                          'name': 'Lexington Rombus',
#                                          'type': 'STORE'},
#                             'position': {'id': '393589', 'name': 'Employee EN'},
#                             'primary': True,
#                             'startDate': '2016-12-07',
#                             'systemGenerated': False}],
#     'email': 'andgo@sharklasers.com',
#     'firstName': 'And',
#     'id': '370129',
#     'language': 'en',
#     'lastName': 'Go',
#     'phoneNumbers': [{}],
#     'status': 'ACTIVE',
#     'username': 'andgo'}
#    ###################### USER END ##########################

#        print("itemas start")
#        for item in event_json['currentEmployments']:
#            print(item)
#        print("itemas end")

        return event_json['currentEmployments'][0]['id']

    def get_user_details(self, companyid, userid):

        if not self.xtoken:
            self.xtoken = self.authenticate()

        url = self.get_user_url(companyid, userid)

        if self.debug:
            print("URL: " + url)

        response = RestUtil.get(url, headers={"X-Token": self.xtoken})

        if(self.debug):
            print("##################### USER START #########################")
            pprint.pprint(response.json())
            print("###################### USER END ##########################")

        if response.status_code == 500:
            pprint.pprint(response.json())
            raise RuntimeError('Retrieving User Details failed: {}'
                               .format(response.status_code))

        return self.user_dto_to_csv(response.json())
