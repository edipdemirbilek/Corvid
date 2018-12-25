#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 20:23:21 2018

@author: edip.demirbilek
"""
import requests


class RestUtil():

    def get_authentication_url(env):
        if env == "qa":
            return "https://qa-api.workjamnp.com/auth/v3"

        return "https://api.workjam.com/auth/v3"

    def get_authentication_data(username, password):
        return {"username": username,
                "password": password}

    def post(url, data):
        return requests.post(url, json=data)

    def authenticate(env, username, password):
        url = RestUtil.get_authentication_url(env)
        data = RestUtil.get_authentication_data(username, password)

        response = RestUtil.post(url, data)
        # pprint.pprint(response.json())

        if response.status_code != 200:
            raise RuntimeError('Authentiction failed: {}'
                               .format(response.status_code))
        print("Authentication is sucessfull.")

        return RestUtil.get_xtoken(response)

    def get_xtoken(response):
        return response.json()['token']

    def get_shifts_url(env):
        return ""

    def get_user_url(env):
        return ""
