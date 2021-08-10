#!/usr/bin/env python
# coding: utf-8


import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
import csv
import numpy as np
from pandas import DataFrame as df
import datetime

stocks_l = ['AAPL', 'MSFT', 'TSM', 'NVDA', 'FB']

def Y_urls(sl:list()) -> list():
    yahoofin = 'https://finance.yahoo.com/quote/'
    su = []
    for s in sl:
        su.append(yahoofin+s)
    return su

stocks_u: list() = Y_urls(stocks_l)

def stock_prices(sl:list(), su: list())-> dict():
    
    price_l = []
    p_d = {}
    for url in su:
        rs = requests.get(url).text
        aapl_soup = bs(rs, 'lxml')
        price_l.append(aapl_soup.find('div', attrs={'id': 'quote-header-info'}).find(attrs={'data-reactid':'49'}).get_text())
    p_d = dict(zip(stocks_l, price_l))
    return p_d

stock_dict: dict() = stock_prices(stocks_l, stocks_u)

s_c = 'Price '+ str(datetime.date.today())

stock_df = df.from_dict(stock_dict, orient='index', columns= [s_c])

stock_df.to_csv('stock_df1.csv')






