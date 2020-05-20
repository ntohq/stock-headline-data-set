#Import request and parse from urllib so we can request from the api
from urllib import request as req
from urllib import parse
#Import json to manipulate api data
import json

class fetchNews():
  def __init__(self):
    self.url = "https://analyst.herokuapp.com/newsQuery/?"
  
  def createQuery(self, ticker):
        self.queryParam = {
            "ticker":str(ticker),          
        }
        self.parseQuery()
    #END

  def parseQuery(self):
        #parse the paramaters
        self.queryParam = parse.urlencode(self.queryParam)
        #create the url with query string
        self.query = self.url + self.queryParam
    #END

  def retrieveQuery(self):
        #query the srtring and the store api's response
        self.apiResp = req.urlopen(self.query)
        #if connection is connected
        if(self.apiResp.isclosed() == False):
            #Store json Data
            self.json = json.load(self.apiResp)
        else:
            raise ValueError('Error: Api Connection Failed')
    #END

  def clean_data(self):
    self.newsData = []

    for i in self.json['articles']:
      if not i['title'] == '' and not i['title'] == 'undefined':
        self.newsData.append([i['title'], i['url']])

  #to make life easy :)
  def autoQuery(self, t):
      self.createQuery(t)
      self.retrieveQuery()
      self.clean_data()
      return(self.newsData)