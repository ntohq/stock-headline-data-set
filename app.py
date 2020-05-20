from data import fetch
from data import news
#from data import compress
import pandas as pd
newsFetch = news.fetchNews()

print("Welcome to analyst's stock news data set for ml")
#enter in the list below all the stocks you want to record
all_tickers = ['INO', 'AAPL', 'VER']

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

  data = {
    'date': 'test',
    'tiker': all_tickers[i],
    'slope': (points[0] - points[1]) / (0 - 1),
    'news': { '':newsFetch.autoQuery(all_tickers[i]) }
  }

  df = pd.DataFrame(data, columns=['date', 'tiker', 'slope', 'news'])
 
  frames.append(df)
  
result = pd.concat(frames)

print(result)