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

    def get_event_allowed_actions(self, event_json):
        try:
            return '_'.join(map(str, event_json['allowedActions']))
        except Exception as e:
            print(e)
            return ''

    def get_event_approval_requests(self, event_json):
#        'approvalRequests': []
        try:
            return ''
        except Exception as e:
            print(e)
            return ''

    def get_event_assignees(self, event_json):
#        'assignees': [{'bookingMethod': 'ASSIGN',
#                    'breaks': [],
#                    'profile': {'firstName': 'And',
#                                'id': '370129',
#                                'lastName': 'Go'},
#                    'status': 'CONFIRMED'}]
        try:
            return ''
        except Exception as e:
            print(e)
            return ''

    def get_event_created_by(self, event_json):
#        'createdBy': {'id': '328237'}
        try:
            return event_json['createdBy']['id']
        except Exception as e:
            print(e)
            return ''

    def get_event(self, event_json):
#        'event': {'endDateTime': '2018-12-27T14:00:00.000+0000',
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
#               'type': 'SHIFT'}
        try:
            return ''
        except Exception as e:
            print(e)
            return ''

    def get_event_external_fields(self, event_json):
#        'externalFields': {'workjam': {'locationExternalCodesMap': {'328038': [None,
#                                                                            None,
#                                                                            None,
#                                                                            '783336']}}}
        try:
            return ''
        except Exception as e:
            print(e)
            return ''

    def get_event_external_id(self, event_json):
        try:
            return event_json['externalId']
        except Exception as e:
            print(e)
            return ''

    def get_event_id(self, event_json):
        try:
            return event_json['id']
        except Exception as e:
            print(e)
            return ''

    def get_event_locked(self, event_json):
        try:
            return str(event_json['id'])
        except Exception as e:
            print(e)
            return ''

    def get_event_offered_spots(self, event_json):
#        'offeredSpots': {'remainingQuantity': 0}
        try:
            return event_json['offeredSpots']['remainingQuantity']
        except Exception as e:
            print(e)
            return ''

    def get_event_open_spots(self, event_json):
#        'openSpots': {'broadcast': False,
#                   'remainingQuantity': 0,
#                   'requiresApproval': False,
#                   'useMarketplace': False,
#                   'useSeniorityList': False}
        try:
            return ''
        except Exception as e:
            print(e)
            return ''

    def get_event_position(self, event_json):
#        'position': {'externalId': '123', 'id': '393589', 'name': 'Employee EN'}
        try:
            return ''
        except Exception as e:
            print(e)
            return ''

    def get_event_quantity(self, event_json):
        try:
            return event_json['quantity']
        except Exception as e:
            print(e)
            return ''

    def get_event_segments(self, event_json):
#        'segments': [{'endDateTime': '2018-12-27T14:00:00.000+0000',
#                   'location': {'id': '328038',
#                                'name': 'Lexington Rombus',
#                                'timeZoneId': 'America/Toronto'},
#                   'position': {'id': '393589', 'name': 'Employee EN'},
#                   'startDateTime': '2018-12-27T13:00:00.000+0000',
#                   'type': 'SHIFT'}]
        try:
            return ''
        except Exception as e:
            print(e)
            return ''

    def get_event_status(self, event_json):
        try:
            return str(event_json['status'])
        except Exception as e:
            print(e)
            return ''

    def event_dto_to_csv(self, event_json):
        return self.get_event_allowed_actions(event_json) + ',' \
    + self.get_event_approval_requests(event_json) + ',' \
    + self.get_event_assignees(event_json) + ',' \
    + self.get_event_created_by(event_json) + ',' \
    + self.get_event(event_json) + ',' \
    + self.get_event_external_fields(event_json) + ',' \
    + self.get_event_external_id(event_json) + ',' \
    + self.get_event_id(event_json) + ',' \
    + self.get_event_locked(event_json) + ',' \
    + self.get_event_offered_spots(event_json) + ',' \
    + self.get_event_open_spots(event_json) + ',' \
    + self.get_event_position(event_json) + ',' \
    + self.get_event_quantity(event_json) + ',' \
    + self.get_event_segments(event_json) + ',' \
    + self.get_event_status(event_json)

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

    def get_user_badge_level_ids(self, event_json):
        try:
            return '_'.join(map(str, event_json['badgeLevelIds']))
        except Exception as e:
            print(e)
            return ''

    def get_user_birth_date(self, event_json):
        try:
            return event_json['birthDate']
        except Exception as e:
            print(e)
            return ''

    def get_user_employment_position(self, event_json):
        return event_json['id'] + ',' \
    + event_json['name']

    def get_user_employment_location(self, event_json):
        return event_json['externalCode'] + ',' \
    + event_json['id'] + ',' \
    + event_json['name'] + ',' \
    + event_json['type']

    def get_user_current_employment(self, event_json):
        return event_json['id'] + ',' \
    + self.get_user_employment_location(event_json['location'])  + ',' \
    + self.get_user_employment_position(event_json['position'])  + ',' \
    + str(event_json['primary']) + ',' \
    + event_json['startDate'] + ',' \
    + str(event_json['systemGenerated'])

    def get_user_next_two_employments(self, other_employments):
        default = ',,,,,,,,,'

        if len(other_employments) == 0:
            return default + ',' + default

        elif len(other_employments) == 1:
            return default + ',' + other_employments[0]

        else:
            return ','.join(other_employments[:2])

    def get_user_current_employments(self, event_json):
        try:
            other_employments = []
            primary_emploment = ''
            for current_employment in event_json['currentEmployments']:
                if (current_employment['primary'] == True):
                    primary_emploment = self.get_user_current_employment(current_employment)
                else:
                    other_employments.append(self.get_user_current_employment(current_employment))

            return primary_emploment + ',' + self.get_user_next_two_employments(other_employments)
        except Exception as e:
            print(e)
            return ''

    def get_user_email(self, event_json):
        try:
            return event_json['email']
        except Exception as e:
            print(e)
            return ''

    def get_user_first_name(self, event_json):
        try:
            return event_json['firstName']
        except Exception as e:
            print(e)
            return ''

    def get_user_id(self, event_json):
        try:
            return event_json['id']
        except Exception as e:
            print(e)
            return ''

    def get_user_language(self, event_json):
        try:
            return event_json['language']
        except Exception as e:
            print(e)
            return ''

    def get_user_last_name(self, event_json):
        try:
            return event_json['lastName']
        except Exception as e:
            print(e)
            return ''

    def get_user_phone_numbers(self, event_json):
        try:
            return '_'.join(map(str, event_json['phoneNumbers']))
        except Exception as e:
            print(e)
            return ''

    def get_user_status(self, event_json):
        try:
            return event_json['status']
        except Exception as e:
            print(e)
            return ''

    def get_user_name(self, event_json):
        try:
            return event_json['username']
        except Exception as e:
            print(e)
            return ''

    def user_dto_to_csv(self, event_json):
        return self.get_user_id(event_json) + ',' \
    + self.get_user_name(event_json) + ',' \
    + self.get_user_first_name(event_json) + ',' \
    + self.get_user_last_name(event_json) + ',' \
    + self.get_user_birth_date(event_json) + ',' \
    + self.get_user_language(event_json) + ',' \
    + self.get_user_phone_numbers(event_json) + ',' \
    + self.get_user_email(event_json) + ',' \
    + self.get_user_status(event_json) + ',' \
    + self.get_user_current_employments(event_json) + ',' \
    + self.get_user_badge_level_ids(event_json)

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
