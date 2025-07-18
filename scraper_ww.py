#! /usr/bin/env python3
##############################################################################
#
#                        Program name: scraper_ww.py
#                        Created:      Sun Jul 06 2025 13:11
#                        author:       Stephen Flowers Chávez
#
##############################################################################
import requests
import json

#downloading json string from URL which gets automatically updated
response = json.loads(requests.get("https://prop.kc2g.com/api/stations.json").text)

#print items of interest in the USA only: MUFD, station, time
print("{:<30} {:<21} {:<20}".format(' Station', ' MUFD', ' Time'))
for item in response:
    mufd = item['mufd']
    name = item['station']['name']
    time = item['time']
    if name.find('')>=0:
         if time.find('2025')>=0:
#        print('Station: ', name, '\t\tMUFD: ', mufd, '\t\tTime: ', time)
#        print("Station: %s, MUFD: %s, Time: %s" % (name, mufd, time))
            print("{:<30} {:<20} {:<20}".format(name, str(mufd), time))
        
        
        
         