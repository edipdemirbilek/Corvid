#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 20:23:21 2018

@author: edip.demirbilek
"""
import requests
import pprint


class RestUtil():

    def get_base_url(env):
        if env == "qa":
            return "https://qa-api.workjamnp.com"

        return "https://api.workjam.com"

    def get_authentication_url(env):
        return RestUtil.get_base_url(env) + "/auth/v3"

    def get_authentication_data(username, password):
        return {"username": username,
                "password": password}

    def post(url, data):
        return requests.post(url, json=data)

    def get(url, headers):
        return requests.get(url, headers=headers)

    def authenticate(env, username, password):
        url = RestUtil.get_authentication_url(env)
        data = RestUtil.get_authentication_data(username, password)

        response = RestUtil.post(url, data)
        # pprint.pprint(response.json())

        if response.status_code != 200:
            pprint.pprint(response.json())
            raise RuntimeError('Authentiction failed: {}'
                               .format(response.status_code))

        return RestUtil.get_xtoken(response)

    def get_event_url(env, companyid, locationid, eventid):
        return  RestUtil.get_base_url(env) + "/api/v4/companies/{}/locations/{}/shifts/{}".format(str(companyid), str(locationid), str(eventid))

    def get_event_details(debug, env, xtoken, companyid, locationid, eventid):
        url = RestUtil.get_event_url(env, companyid, locationid, eventid)

        if debug:
            print("URL: "+ url)

        response = RestUtil.get(url, headers={"X-Token": xtoken})

        if(debug):
            print("#################### EVENT START #########################")
            pprint.pprint(response.json())
            print("##################### EVENT END ##########################")

        if response.status_code == 500:
            raise RuntimeError('Retrieving Event Details failed: {}'
                               .format(response.status_code))

        return response

    def get_xtoken(response):
        return response.json()['token']

    def get_user_url(env, companyid, userid):
            return  RestUtil.get_base_url(env) + "/api/v4/companies/{}/employees/{}".format(str(companyid), str(userid))

    def get_user_details(debug, env, xtoken, companyid, userid):
        url = RestUtil.get_user_url(env, companyid, userid)

        if debug:
            print("URL: "+ url)

        response = RestUtil.get(url, headers={"X-Token": xtoken})

        if(debug):
            print("##################### USER START #########################")
            pprint.pprint(response.json())
            print("###################### USER END ##########################")

        if response.status_code == 500:
            raise RuntimeError('Retrieving User Details failed: {}'
                               .format(response.status_code))

        return response
