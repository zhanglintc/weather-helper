#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

# open sample weather data stored in WeatherData.json
fr = open('../dat/GeoData.json')

# read data
jsonData = fr.read()

# parse
parsed_json = json.loads(jsonData)

# print useful data
for i in range(len(parsed_json['results'][1]['address_components'])):
    if parsed_json['results'][1]['address_components'][i]['types'][0] == "country":
        print ("country name: " + parsed_json['results'][1]['address_components'][i]['long_name'])
    if parsed_json['results'][1]['address_components'][i]['types'][0] == "locality":
        print ("city name: " + parsed_json['results'][1]['address_components'][i]['long_name'])
    if parsed_json['results'][1]['address_components'][i]['types'][0] == "sublocality_level_1":
        print ("district name: " + parsed_json['results'][1]['address_components'][i]['long_name'])


