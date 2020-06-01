from data import fetch
from data import news
#from data import compress
import pandas as pd
import datetime
from dotenv import load_dotenv

load_dotenv()

newsFetch = news.fetchNews()


print("Welcome to analyst's stock news data set for ml")
#enter in the list below all the stocks you want to record
all_tickers = ['PFE', 'INO', 'SNY', 'NVS', 'CVX', 'OXY', 'FSLR', 'XOM', 'SM', 'HAL', 'AVB', 'EXR', 'MAC', 'AAPL', 'MSFT', 'FB', 'ATVI']

#stock var paramaters
params = {
  'interval': '1m',
  'period': '1d',
  'dir':None
}

frames = []

for i in range(len(all_tickers)):
  #fetch the start and end point for the stock 
  points = (fetch.get(
    all_tickers[i],
    params["period"],
    params["interval"]
    ))
  #fetch news on stock
  news = newsFetch.autoQuery(fetch.getName(all_tickers[i]))

  data = pd.Series([all_tickers[i], (points[0] - points[1]) / (0 - 1), news])
  #create Data Frame
  df = pd.DataFrame([list(data)], columns=['tiker', 'slope', 'news'], index=[str(datetime.datetime.now().strftime("%m-%d-%Y"))])
  #append data frame into Array
  frames.append(df)
#concat the results of all data frames
result = pd.concat(frames)
#print results

try: 
  result.to_csv('data.csv', mode='a')
  print(pd.read_csv('data.csv'))
except:
  try:
    result.to_csv('data.csv')
  except OSError as err:
      print(err)
