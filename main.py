import urllib.request
import json
import os
import sys
import pandas as pd
import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import matplotlib.pyplot as plt
import plotly_express as px
import tqdm
from tqdm.notebook import tqdm_notebook
import sched, time
import requests
from bs4 import BeautifulSoup
s = sched.scheduler(time.time, time.sleep)

def get_location():
        req = urllib.request.Request("http://api.open-notify.org/iss-now.json")
        response = urllib.request.urlopen(req)

        obj = json.loads(response.read())

        locator = Nominatim(user_agent="myGeocoder")
        coordinates = obj['iss_position']['latitude'], obj['iss_position']['longitude']

        location = locator.reverse(coordinates)


        
        print ("The Internation Space Station is currently located at the following cordinates: ")
        result1 = (print ("Latitude: " + obj['iss_position']['longitude']))
        result2 = (print ("Latitude: " + obj['iss_position']['longitude']))
          

        s.enter(1, 1, get_location)

        with open('result.txt', 'w') as f:
          f.write (str("Latitude: " + obj['iss_position']['latitude']+ "\n"))
          f.write (str("Longitude: " + obj['iss_position']['longitude']))



s.enter(1, 1, get_location)
s.run()
