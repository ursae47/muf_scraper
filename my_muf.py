#! /usr/bin/env python3
##############################################################################
#
#                        Program name: my_muf.py
#                        Created:      Sun Jan 25 2023 11:00
#                        author:       Stephen Flowers Chávez
#
##############################################################################
import pandas as pd

#reading flat file using pandas
muf_data = pd.read_csv('data.txt', sep="\t" )

#set a minimum threshold frequency
muf = muf_data[(muf_data['MUFD']>14.150)]

#print(muf)
#i want to only print out or output USA stations
only_USA_Stations = muf.loc[muf['Station'].str.contains('USA')]

#print the USA stations
print(only_USA_Stations[['Station', 'Time', 'MUFD']].sort_values("MUFD", ascending = False))

#finally write out to file format our output
only_USA_Stations.to_csv("modified_data.csv", index = False)
