import os
import time
import yfinance as yf
import dateutil.relativedelta
from datetime import date
import datetime
import numpy as np
import sys
from tqdm import tqdm
import requests
import json

Current_club=requests.get("http://api.clubelo.com/Bayern")
data=Current_club.text
years=data.split(",")
for i,value in enumerate(years):
    print(i,value)
    print(type(value))
    
