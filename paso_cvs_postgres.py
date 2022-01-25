#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('postgresql://tradedetail:tradedetail@bvmnglapsboxp01.nngg.corp:5432/tradedetail', client_encoding='utf-8', echo=False)


# In[20]:


datos = pd.read_csv("bot.csv",sep = ';')
datos.head(30)


# In[21]:


datos.to_sql('bot', engine,  if_exists='append')


# In[22]:


import psycopg2
import pandas as pd
import pandas.io.sql as psql

conn = psycopg2.connect(database="tradedetail", user="tradedetail", password="tradedetail", host="bvmnglapsboxp01.nngg.corp", port="5432",client_encoding='utf-8')
cur = conn.cursor()
df = psql.read_sql("Select tom from bot where SecCode = 'BE0000350596'", conn)
df.head(5)


# In[25]:


print(df.iloc[0]['tom'])



# In[27]:


import re

string = "Hey! What's up?"
string = re.sub("\[|\'|\?","",string)
print(string)


# In[ ]:




