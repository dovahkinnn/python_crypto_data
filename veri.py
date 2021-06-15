from binance.client import Client
from binance.enums import *
import numpy as np
import pandas as pd
import time
from os import system
import datetime

# CONNECTION
filename = 'credentials.txt'
lines = [line.rstrip('\n') for line in open(filename)]
key = lines[0]
secret = lines[1]
client = Client(key, secret)

# CONFIGURATION
interval = '5m'
limit = 1000


klines = client.get_klines(symbol="WINUSDT", interval=interval, limit=limit)
close = [float(entry[4]) for entry in klines]
prices = np.array(close, dtype=float)
dates = [datetime.datetime.fromtimestamp(int(entry[6]/1000)) for entry in klines]
closeDates = np.array(dates, dtype=str)

klines2 = client.get_klines(symbol="DOGEUSDT", interval=interval, limit=limit)
close2 = [float(entry[4]) for entry in klines2]
prices2 = np.array(close2, dtype=float)
dates2 = [datetime.datetime.fromtimestamp(int(entry[6]/1000)) for entry in klines2]
closeDates2 = np.array(dates2, dtype=str)

d = { 'Dates':closeDates,'Coin':'','Prices':prices}
df = pd.DataFrame(d)
df['Coin'] = 'WIN'
d2 = { 'Dates':closeDates2,'Coin':'','Prices':prices2}
df2 = pd.DataFrame(d2)
df2['Coin'] = 'DOGE'

print(df)

df.to_csv('datass.csv', encoding='utf-8',index=False)
df2.to_csv('datass.csv',encoding="utf-8",index=False, header=False,mode="a")