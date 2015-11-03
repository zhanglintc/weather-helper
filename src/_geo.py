#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import json

def getGeoInfo(lat, lng):
    # "http://maps.google.cn/maps/api/geocode/json?latlng=31.02,109.47"
    queryURL = "http://maps.google.cn/maps/api/geocode/json?latlng={0},{1}".format(lat, lng)

    response = urllib.urlopen(queryURL)
    json_string = response.read()
    parsed_json = json.loads(json_string)

    return parsed_json

if __name__ == "__main__":
    lat = "31.02"
    lng = "109.47"
    print getGeoInfo(lat, lng)