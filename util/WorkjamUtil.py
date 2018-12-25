#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 20:23:21 2018

@author: edip.demirbilek
"""


class WorkjamUtil():

    def get_event_header_csv():
        return ""

    def event_dto_to_csv(event_dto):
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

    def get_user_header_csv():
        return ""

    def user_dto_to_csv(event_json):
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
