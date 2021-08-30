import pandas as pd

import requests as re
import json 
from IPython.display import JSON
from config import ApiKey
from itertools import chain

df = pd.read_csv('DataPreparation/Heavy_Data/flightsprocessed.csv')

def weather(x):
    r = []
    for i in x.index:
        params = {'location': x['origin_city_name'][i],'startDateTime': x['fl_date'][i],'endDateTime': x['fl_date'][i]}
        weather = re.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/history?aggregateHours=24&combinationMethod=aggregate&maxStations=-1&maxDistance=-1&contentType=json&unitGroup=metric&locationMode=single&key={ApiKey}&dataElements=default&',params=params)
        z = weather.json()
        r.append(z)
    return r

# Obtaining the weather data and joining it

temp = weather(df)
t = []
for i in temp:
    t.append(i['location']['values'])
    
temp_df = pd.DataFrame(t)
weather_data = pd.concat([df,temp_df],axis = 1)

pd.DataFrame.to_csv(weather_data,'weather_data.csv',index=False)