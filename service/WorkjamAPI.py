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

    def get_xtoken(self, response):
        return response.json()['token']

    def get_event_url(self, companyid, locationid, eventid):
        return self.get_base_url() + "/api/v4/companies/{}/locations/{}/shifts/{}".format(str(companyid), str(locationid), str(eventid))

    def get_event_allowed_actions(self, header, event_json):
        if header:
            return 'event_allowed_actions'

        try:
            return '_'.join(map(str, event_json['allowedActions']))
        except Exception as e:
            print(e)
            return ''

    def get_event_approval_requests(self, header, event_json):
        if header:
            return 'event_approval_requests'

# for now we do nothing with this
#        'approvalRequests': []
        try:
            return ''
        except Exception as e:
            print(e)
            return ''

    def get_event_assignees(self, header, event_json):
        if header:
            return 'event_assignees'

# for the moment we do nothing with this
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

    def get_event_created_by(self, header, event_json):
        if header:
            return 'event_created_by'

        try:
            return str(event_json['createdBy']['id'])
        except Exception as e:
            print(e)
            return ''

    def get_event_location(self, header, event_json):
        if header:
            return 'event_location_external_code,' \
        + 'event_location_external_id,' \
        + 'event_location_id,' \
        + 'event_location_name,' \
        + 'event_location_timezone_id,' \
        + 'event_location_type'

        try:
            return str(event_json['externalCode']) + ',' \
        + str(event_json['externalId']) + ',' \
        + str(event_json['id']) + ',' \
        + str(event_json['name']) + ',' \
        + str(event_json['timeZoneId']) + ',' \
        + str(event_json['type'])

        except Exception as e:
            print(e)
            return ',,,,,'

    def get_event(self, header, event_json):
        if header:
            return 'event_end_date_time,' \
        + 'event_id,' \
        + self.get_event_location(header, '') \
        + ',event_note,' \
        + 'event_recurrence,' \
        + 'event_start_date_time,' \
        + 'event_title,' \
        + 'event_type'

        try:
            event = event_json['event']

            return str(event['endDateTime']) + ',' \
        + str(event['id']) + ',' \
        + self.get_event_location(header, event['location']) + ',' \
        + str(event['note']) + ',' \
        + str(event['recurrence']) + ',' \
        + str(event['startDateTime']) + ',' \
        + str(event['title']) + ',' \
        + str(event['type'])

        except Exception as e:
            print(e)
            return ',,,,,,,,,,,,'

    def get_event_external_fields(self, header, event_json):
        if header:
            return 'event_external_fields'

# for now we do not need these fields
#        'externalFields': {'workjam': {'locationExternalCodesMap': {'328038': [None,
#                                                                            None,
#                                                                            None,
#                                                                            '783336']}}}
        try:
            return ''
        except Exception as e:
            print(e)
            return ''

    def get_event_external_id(self, header, event_json):
        if header:
            return 'event_external_id'

        try:
            return str(event_json['externalId'])
        except Exception as e:
            print(e)
            return ''

    def get_event_id(self, header, event_json):
        if header:
            return 'event_id'

        try:
            return str(event_json['id'])
        except Exception as e:
            print(e)
            return ''

    def get_event_locked(self, header, event_json):
        if header:
            return 'event_locked'

        try:
            return str(event_json['locked'])
        except Exception as e:
            print(e)
            return ''

    def get_event_offered_spots(self, header, event_json):
        if header:
            return 'event_offered_spots'

        try:
            return str(event_json['offeredSpots']['remainingQuantity'])
        except Exception as e:
            print(e)
            return ''

    def get_event_open_spots(self, header, event_json):
        if header:
            return 'event_open_spots_broadcast,' \
        + 'event_open_spots_remaining_quantity,' \
        + 'event_open_spots_requires_approval,' \
        + 'event_open_spots_use_marketplace,' \
        + 'event_open_spots_use_seniority_list'

        try:
            open_spots = event_json['openSpots']
            return str(open_spots['broadcast']) + ',' \
        + str(open_spots['remainingQuantity']) + ',' \
        + str(open_spots['requiresApproval']) + ',' \
        + str(open_spots['useMarketplace']) + ',' \
        + str(open_spots['useSeniorityList'])

        except Exception as e:
            print(e)
            return ',,,,'

    def get_event_position(self, header, event_json):
        if header:
            return 'event_position_external_id,'\
        + 'event_position_id,'\
        + 'event_position_name'

        try:
            position = event_json['position']
            return str(position['externalId']) + ',' \
        + str(position['id']) + ',' \
        + str(position['name'])

            return ''
        except Exception as e:
            print(e)
            return ',,'

    def get_event_quantity(self, header, event_json):
        if header:
            return 'event_quantity'

        try:
            return str(event_json['quantity'])
        except Exception as e:
            print(e)
            return ''

    def get_event_segments(self, header, event_json):
        if header:
            return 'event_segments_size'

# for now we do not care about the number of segments yet

#        'segments': [{'endDateTime': '2018-12-27T14:00:00.000+0000',
#                   'location': {'id': '328038',
#                                'name': 'Lexington Rombus',
#                                'timeZoneId': 'America/Toronto'},
#                   'position': {'id': '393589', 'name': 'Employee EN'},
#                   'startDateTime': '2018-12-27T13:00:00.000+0000',
#                   'type': 'SHIFT'}]
        try:
            segments = []
            for segment in event_json['segments']:
                segments.append(segment)

                return str(len(segments))

            return ''
        except Exception as e:
            print(e)
            return ''

    def get_event_status(self, header, event_json):
        if header:
            return 'event_status'

        try:
            return str(event_json['status'])
        except Exception as e:
            print(e)
            return ''

    def event_dto_to_csv(self, header, event_json):
        return self.get_event_allowed_actions(header, event_json) + ',' \
    + self.get_event_approval_requests(header, event_json) + ',' \
    + self.get_event_assignees(header, event_json) + ',' \
    + self.get_event_created_by(header, event_json) + ',' \
    + self.get_event(header, event_json) + ',' \
    + self.get_event_external_fields(header, event_json) + ',' \
    + self.get_event_external_id(header, event_json) + ',' \
    + self.get_event_id(header, event_json) + ',' \
    + self.get_event_locked(header, event_json) + ',' \
    + self.get_event_offered_spots(header, event_json) + ',' \
    + self.get_event_open_spots(header, event_json) + ',' \
    + self.get_event_position(header, event_json) + ',' \
    + self.get_event_quantity(header, event_json) + ',' \
    + self.get_event_segments(header, event_json) + ',' \
    + self.get_event_status(header, event_json)

    def get_event_details(self, header, companyid, locationid, eventid):

        if header:
            return self.event_dto_to_csv(header, "")

        if not self.xtoken:
            self.xtoken = self.authenticate()

        url = self.get_event_url(companyid, locationid, eventid)

        if self.debug:
            print("URL: " + url)

        response = RestUtil.get(url, headers={"X-Token": self.xtoken})

        if(self.debug):
            print("#################### EVENT START #########################")
            pprint.pprint(response.json())
            print("##################### EVENT END ##########################")

        if response.status_code != 200:
            # pprint.pprint(response.json())
            raise RuntimeError('\nRetrieving Event Details failed!!!\n Response from Workjam Server: {} for: {}\n'
                               .format(response.status_code, url))

        return self.event_dto_to_csv(header, response.json())

    def get_user_url(self, companyid, userid):
            return self.get_base_url() + "/api/v4/companies/{}/employees/{}".format(str(companyid), str(userid))

    def get_user_badge_level_ids(self, header, event_json):
        if header:
            return 'user_badge_level_ids'

        try:
            return ''
            # to0  many
            #return '_'.join(map(str, event_json['badgeLevelIds']))
        except Exception as e:
            print(e)
            return ''

    def get_user_birth_date(self, header, event_json):
        if header:
            return 'user_birth_date'

        try:
            return str(event_json['birthDate'])
        except Exception as e:
            print(e)
            return ''

    def get_user_employment_position(self, header, counter, event_json):
        if header:
            return 'user_employment_' + str(counter) + '_position_id,' \
                 + 'user_employment_' + str(counter) + '_position_name'
        try:
            return event_json['id'] + ',' + event_json['name']
        except Exception as e:
            print(e)
            return ','

    def get_user_employment_location(self, header, counter, event_json):
        if header:
            return 'user_employment_' + str(counter) + '_location_external_code,' \
                 + 'user_employment_' + str(counter) + '_location_id,' \
                 + 'user_employment_' + str(counter) + '_location_name,' \
                 + 'user_employment_' + str(counter) + '_location_type'
        try:
            return event_json['externalCode'] + ',' \
        + event_json['id'] + ',' \
        + event_json['name'] + ',' \
        + event_json['type']
        except Exception as e:
            print(e)
            return ',,,'

    def get_user_current_employment(self, header, counter, event_json):
        if header:
            return 'user_employment_' + str(counter) + '_id,' \
        + self.get_user_employment_location(header, counter, '') + ',' \
        + self.get_user_employment_position(header, counter, '') \
        + ',user_employment_' + str(counter) + '_primary,' \
        + 'user_employment_' + str(counter) + '_start_date,' \
        + 'user_employment_' + str(counter) + '_system_generated'

        try:
            return event_json['id'] + ',' \
        + self.get_user_employment_location(header, counter, event_json['location'])  + ',' \
        + self.get_user_employment_position(header, counter, event_json['position'])  + ',' \
        + str(event_json['primary']) + ',' \
        + event_json['startDate'] + ',' \
        + str(event_json['systemGenerated'])
        except Exception as e:
            print(e)
            return ',,,,,,,,'

    def get_user_next_two_employments(self, other_employments):
        default = ',,,,,,,,,'

        if len(other_employments) == 0:
            return default + ',' + default

        elif len(other_employments) == 1:
            return default + ',' + other_employments[0]

        else:
            return ','.join(other_employments[:2])

    def get_user_current_employments(self, header, event_json):
        if header:
            return self.get_user_current_employment(header, 1, "") + ',' \
        + self.get_user_current_employment(header, 2, "") + ',' \
        + self.get_user_current_employment(header, 3, "")

        try:
            other_employments = []
            primary_emploment = ''
            for current_employment in event_json['currentEmployments']:
                if current_employment['primary']:
                    primary_emploment = self.get_user_current_employment(
                            header, 0, current_employment)
                else:
                    other_employments.append(self.get_user_current_employment(
                            header, 0, current_employment))

            return primary_emploment + ',' \
                + self.get_user_next_two_employments(other_employments)

        except Exception as e:
            print(e)
            return ',,,,,,,,,,,,,,,,,,,,,,,,,,,,,'

    def get_user_email(self, header, event_json):
        if header:
            return 'user_email'

        try:
            return str(event_json['email'])
        except Exception as e:
            print(e)
            return ''

    def get_user_first_name(self, header, event_json):
        if header:
            return 'user_first_name'

        try:
            return str(event_json['firstName'])
        except Exception as e:
            print(e)
            return ''

    def get_user_id(self, header, event_json):
        if header:
            return 'user_id'

        try:
            return str(event_json['id'])
        except Exception as e:
            print(e)
            return ''

    def get_user_language(self, header, event_json):
        if header:
            return 'user_language'

        try:
            return str(event_json['language'])
        except Exception as e:
            print(e)
            return ''

    def get_user_last_name(self, header, event_json):
        if header:
            return 'user_last_name'

        try:
            return str(event_json['lastName'])
        except Exception as e:
            print(e)
            return ''

    def get_user_phone_numbers(self, header, event_json):
        if header:
            return 'user_phone_numbers'

        try:
            return '_'.join(map(str, event_json['phoneNumbers']))
        except Exception as e:
            print(e)
            return ''

    def get_user_status(self, header, event_json):
        if header:
            return 'user_status'

        try:
            return str(event_json['status'])
        except Exception as e:
            print(e)
            return ''

    def get_user_name(self, header, event_json):
        if header:
            return 'user_name'

        try:
            return str(event_json['username'])
        except Exception as e:
            print(e)
            return ''

    def user_dto_to_csv(self, header, event_json):
        return self.get_user_id(header, event_json) + ',' \
    + self.get_user_name(header, event_json) + ',' \
    + self.get_user_first_name(header, event_json) + ',' \
    + self.get_user_last_name(header, event_json) + ',' \
    + self.get_user_birth_date(header, event_json) + ',' \
    + self.get_user_language(header, event_json) + ',' \
    + self.get_user_phone_numbers(header, event_json) + ',' \
    + self.get_user_email(header, event_json) + ',' \
    + self.get_user_status(header, event_json) + ',' \
    + self.get_user_current_employments(header, event_json) + ',' \
    + self.get_user_badge_level_ids(header, event_json)

    def get_user_details(self, header, companyid, userid):

        if header:
            return self.user_dto_to_csv(header, "")

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

        if response.status_code != 200:
            # pprint.pprint(response.json())
            raise RuntimeError('\nRetrieving User Details failed!!!\n Response from Workjam Server: {} for: {}\n'
                               .format(response.status_code, url))

        return self.user_dto_to_csv(header, response.json())
