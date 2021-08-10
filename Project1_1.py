#!/usr/bin/env python
# coding: utf-8


import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
import csv
import numpy as np
from pandas import DataFrame as df
import datetime

#yahoofin = 'https://finance.yahoo.com/quote/'

stocks_l = ['AAPL', 'MSFT', 'TSM', 'NVDA', 'FB']
stocks_u = []

#appleinc = 'AAPL'

def Y_urls(sl:list(), su: list() ) -> list():
    yahoofin = 'https://finance.yahoo.com/quote/'
    for s in sl:
        su.append(yahoofin+s)

stock = yahoofin+appleinc
stock

def stock_price(stock_url: str)-> str:
    y_aapl = requests.get(stock_url).text
    aapl_soup = bs(y_aapl, 'lxml')
    price = aapl_soup.find('div', attrs={'id': 'quote-header-info'}).find(attrs={'data-reactid':'49'}).get_text()
    return price

sp = stock_price(stock)

aapl_dframe2 = pd.DataFrame({appleinc:[sp]}, index = [datetime.date.today()])
aapl_dframe2 = aapl_dframe2.transpose()
aapl_dframe2

aapl_dframe2.to_csv('aapl_p.csv')


