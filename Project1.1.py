#!/usr/bin/env python
# coding: utf-8


import requests




import pandas as pd


from bs4 import BeautifulSoup as bs


import csv


import numpy as np


from pandas import DataFrame as df


import datetime


yahoofin = 'https://finance.yahoo.com/quote/'


appleinc = 'AAPL'


y_aapl = requests.get(yahoofin+appleinc)
y_aapl = y_aapl.text


# In[11]:


aapl_soup = bs(y_aapl, 'lxml')


# In[12]:


price = aapl_soup.find('div', attrs={'id': 'quote-header-info'}).find(attrs={'data-reactid':'49'})
price = price.get_text()
price


# In[13]:


aapl_table = pd.Series([price], index=[appleinc])
aapl_table


# In[15]:


aapl_dframe = pd.DataFrame({appleinc:[price]}, index = [datetime.date.today()])  #np.arange(len(list(appleinc))
aapl_dframe = aapl_dframe.transpose()
aapl_dframe




aapl_dframe.to_csv('aapl_2.csv')
=

pd.DataFrame({datetime.date.today():[price]}, index = [appleinc])

