#Import request and parse from urllib so we can request from the api
from urllib import request as req
#Import json to manipulate api data
import json
#import pandas
import pandas as pd
#Import yfinance api lib
import yfinance as yf

def get(ticker, p, i):
  stock = yf.Ticker(ticker)
  stock = stock.history(period=p,interval=i)
  df = pd.DataFrame(stock)
  return([df.iloc[0]['High'], df.iloc[len(df) - 1]['High']])

def getName(ticker):
  query = 'https://analyst-server.herokuapp.com/searchQuery/?ticker=' + str(ticker)

  #query the srtring and the store api's response
  apiResp = req.urlopen(query)
  #if connection is connected
  if(apiResp.isclosed() == False):
      #Store json Data
      data_json = json.load(apiResp)

      for i in list(data_json['ticker_data']):
        if i['symbol'] == ticker:
          return(i['name'])
  else:
      raise ValueError('Error: Api Connection Failed')

def organize():
  print('test')