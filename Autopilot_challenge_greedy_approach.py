#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import numpy as np
import pandas as pd

def distance(lat1d, lon1d, lat2d, lon2d): 
    lat1 = math.radians(lat1d)
    lon1 = math.radians(lon1d)
    lat2 = math.radians(lat2d)
    lon2 = math.radians(lon2d)
    R = 6356.752
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance
    
df = pd.read_csv('network.csv', header=None)
arr = df.to_numpy()

start, dest = map(str, input().split())
start_index = np.where(arr==start)
dest_index = np.where(arr==dest)
arr_start = arr[start_index[0]][:]
arr_dest = arr[dest_index[0]][:]

station_names = {}
distance_list = []
for station in arr:
    dist = distance(arr_start[0][1], arr_start[0][2], station[:][1], station[:][2])
    distance_list.append(dist)
    station_names.update({station[0]:dist})
distance_list.sort()
sd = distance(arr_start[0][1], arr_start[0][2], arr_dest[0][1],arr_dest[0][2])
sd_index = distance_list.index(sd)
sd_distance_list = np.array(distance_list[:sd_index])

cc = []
charger_names = []
def recharge(n, x, rangee):
    current_charge = 0
    # num_of_charges  = 0
    previous_charge = 0
    while current_charge < (n-1):
        previous_charge = current_charge
        while((x[current_charge+1] - x[previous_charge]) <= rangee):
            current_charge += 1
            if current_charge == (n-1):
                break
        if current_charge == previous_charge:
            print('Not possible')
        if current_charge < (n-1):
            cc = x[current_charge]
            for name, dist in station_names.items():
                if dist == cc:
                    charger_names.append(name)   
            # num_of_charges += 1 
    return(charger_names) 
            
recharge(len(sd_distance_list), sd_distance_list, 320)

arr_charger = []
for name in charger_names:
    charger_index = np.where(arr==name)
    arr_charger.append(arr[charger_index[0]][:])

printt = [start]
for charger in arr_charger:
    printt.append(charger[0][0])
    printt.append(320/charger[0][3])
printt.append(dest)
    
print(*printt, sep=', ')
