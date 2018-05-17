
# coding: utf-8

# In[1]:


import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import json
from lxml.html import parse,soupparser
from lxml import objectify
from urllib import *


# In[17]:


# JSON数据
obj = """
{"name":"Wes",
"places_lived":["United Statrs","Spain","Germany"],
"pet":null,
"siblings":[{"name":"Scott","age":25,"pet":"Zuko"},
            {"name":"Katie","age":33,"pet":"Cisco"}]
}
"""


# In[18]:


# 通过 json标准库可以将JSON字符串转化为python形式
result = json.loads(obj)
result


# In[19]:


# 使用dumps则将python对象转换成json格式
asjson = json.dumps(result)
asjson


# In[20]:


# 将json对象转换为DataFrame
siblings = DataFrame(result['siblings'],columns=['name','age'])
siblings


# In[3]:


# Web信息收集（XML和HTML）
parsed = (request.urlopen('https://finance.yahoo.com/quote/AAPL/options?ltr=1'))
parsed


# In[5]:


doc  = parsed.read()
doc


# In[8]:


# 使用XPath进行查询
# links = doc.findall('.//a')
# links[15:20]

