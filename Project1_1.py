import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
import csv
import numpy as np
from pandas import DataFrame as df
import datetime

#creates a list of urls based on set of company tickers given.
def y_urls(sl:list()) -> list():
    yahoofin = 'https://finance.yahoo.com/quote/'
    su = []
    for s in sl:
        su.append(yahoofin+s)
    return su

#requests and scrapes the price at the current moment for each company. 
def price_list(su: list()):
    price_l = []
    for url in su:
        rs = requests.get(url).text
        aapl_soup = bs(rs, 'lxml')
        price_l.append(aapl_soup.find('div', attrs={'id': 'quote-header-info'}).find(attrs={'data-reactid':'49'}).get_text())
    return price_l

#create dataframe from price list, and stock list.
def stock_dframe(price_l: list(), sl: list()):
    l_df = df(price_l, index = sl, columns = [datetime.date.today()])
    return l_df

# update dataframe from price list, and stock list.
def update_df(dframe, price_l):
    dframe[datetime.date.today()] = price_l
    return dframe


stock_list = ['AAPL', 'MSFT', 'TSM', 'NVDA', 'FB']

price_df = df(index=stocks_list)

stock_urls : list() = y_urls(stock_list)

prices_: list() = price_list(stock_urls)

stock_df = stock_dframe(prices_, stock_list)

upated_stock_df = update_df(stock_df, price_list)

csv_file_name = 'stock_df1.csv'

stock_df.to_csv(csv_file_name)





