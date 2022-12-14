#! /usr/bin/env python3

import requests
import json

#downloading json string from URL which gets automatically updated
response = json.loads(requests.get("https://prop.kc2g.com/api/stations.json").text)

#print items of interest in the USA only: MUFD, station, time
for item in response:
    mufd = item['mufd']
    name = item['station']['name']
    time = item['time']
    if name.find('USA')>=0:
        print('Station: ', name, '\t\tMUFD: ', mufd, '\t\tTime: ', time)

