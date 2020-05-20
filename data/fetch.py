#import pandas
import pandas as pd
#Import yfinance api lib
import yfinance as yf

def get(ticker, p, i):
  stock = yf.Ticker(ticker)
  stock = stock.history(period=p,interval=i)
  df = pd.DataFrame(stock)
  return([df.iloc[0]['High'], df.iloc[len(df) - 1]['High']])

def organize():
  print('test')