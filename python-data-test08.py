
# coding: utf-8

# In[23]:


# 数据规整化：清理。转换。合并。重塑
from pandas import DataFrame,Series
import pandas as pd
import numpy as np
import re
import json


# In[2]:


# 数据库风格的DataFrame合并
# 数据集的合并(merge)或连接(join)运算是通过一个或多个键将行链接起来的。
# 这些运算是关系型数据库的核心
df1 = DataFrame({'key':['b','b','a','c','a','a','b'],
                'data1':range(7)})
df1


# In[3]:


df2 = DataFrame({'key':['a','b','d'],
                'data2':range(3)})
df2


# In[4]:


# 使用多对一的合并
pd.merge(df1,df2,on='key')


# In[5]:


# 如果两个对象的列名不同，也可以分辨进行制定
df3 = DataFrame({'lkey':['b','b','a','c','a','a','b'],
                'data1':range(7)})
df4 = DataFrame({'rkey':['a','b','d'],
                'data2':range(3)})
pd.merge(df3,df4,left_on='lkey',right_on='rkey')


# In[6]:


# 使用外链接
pd.merge(df1,df2,how='outer')


# In[7]:


# merge的参数
# on 用于连接的列名，必须存在于左右两个DataFrame对象中
# left_on 左侧DataFrame中用作连接键的列
# right_on 右侧DataFrame中用作连接键的列
# left_index 将左侧的行索引用作其连接键
# sort 排序，默认为true


# In[8]:


# 字符串操作
val = 'a,b, guido'
val.split(',')


# In[9]:


pieces = [x.strip() for x in val.split(',')]
pieces


# In[10]:


first, second, third = pieces


# In[11]:


'::'.join(pieces)


# In[12]:


# pandas中矢量化的字符串函数
data = {
    'Dave':'dave@google.com','Steve':'steve@gmail.com',
    'Rob':'rob@gmail.com','Wes':np.nan
}
data = Series(data)
data


# In[14]:


data.isnull()


# In[15]:


# 通过str.contains来检查各个邮箱地址是否含有gmail
data.str.contains('gmail')


# In[17]:


# 当然也可以使用正则表达式，还可以加上任意re选项
pattern = '([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\\.([A-Z]{2,4})'


# In[21]:


data.str.findall(pattern,flags=re.IGNORECASE)


# In[22]:


# 于原生字符串操作大同小异

