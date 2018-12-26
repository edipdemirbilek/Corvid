#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 20:23:21 2018

@author: edip.demirbilek
"""
import requests


class RestUtil():

    def post(url, data):
        return requests.post(url, json=data)

    def get(url, headers):
        return requests.get(url, headers=headers)
