
# coding: utf-8

# In[29]:


# 层次化索引
import datetime
from pandas import Series,DataFrame
import pandas as pd
import numpy as np
import pandas_datareader.data as web

# 层次化索引是一项重要的功能
# 可以使你在一个轴上拥有多个索引级别（可以以低维度形式处理高维度数据）
# 简单例子


# In[2]:


data = Series(np.random.randn(10),
             index=[list('aaabbbccdd'),[1,2,3,1,2,3,1,2,2,3]])
data


# In[3]:


# 使用fillna可以填充缺失的数据（NaN的元素）
# 上面是带有MultiIndex索引的Series的格式化输出形式
data.index


# In[4]:


# 在层次化索引对象中选取数据子集
data['b']


# In[5]:


data['b':'c']


# In[6]:


data.loc[['b','d']]


# In[7]:


#  在内层中进行选取
data[:,2]


# In[8]:


# 层次化索引可以应用于数据重塑和基于分组的操作
# 使用unstack可以将Series重新安排到一个DataFrame中
data.unstack()


# In[9]:


# unstack的逆运算是stack
data.unstack().stack()


# In[10]:


# 对于一个DataFrame，每条轴都可以有分层索引
frame = DataFrame(np.arange(12).reshape((4,3)),
                 index=[list('aabb'),[1,2,1,2]],
                 columns=[['Ohio','Ohio','Colorado'],
                         ['Green','Red','Green']])
frame


# In[11]:


# 各层都可以有名字（可以是字符串，也可以是别的python对象）。
# 如果指定了名称，就会显示在控制台输出中
# 不要将索引名称和轴标签混为一谈！
frame.index.names = ['key1','key2']
frame.columns.names = ['state','color']
frame


# In[12]:


# 根据索引可以轻松选取列分组哦
frame['Ohio']


# In[13]:


# 重排分级顺序
# swaplevel接受两个级别编号或名称，并返回一个互换了级别的新对象（数据不发生变化）
frame.swaplevel('key1','key2')


# In[14]:


# sortlevel则根据单个级别中的值对数据进行排序（稳定的）。
# 交换级别时，常常也会用到sortlevel，这样最终结果就是有序的了
# 现在使用sort_index
frame.sort_index(1)


# In[15]:


frame.swaplevel(0,1).sort_index(0)


# In[16]:


# 许多对DataFrame和Series的描述和汇总的统计都有一个level
# 可以根据行或列上的级别来进行求和
frame.sum(level='key2')


# In[17]:


frame.sum(level='color',axis=1)


# In[18]:


# 这其实是利用了pandas的groupby功能。


# In[19]:


# 使用dataframe的列
# 人们经常想要将DataFrame的一个列或多个列当做行索引来用，或者可能希望
# 将行索引变成Dataframe的列。以下面这个DataFrame为例：
frame = DataFrame({
    'a':range(7),'b':range(7,0,-1),
    'c':['one','one','one','two','two','two','two'],
    'd':[0,1,2,0,1,2,3]
})
frame


# In[20]:


# DataFrame的set_index函数会将其一个或多个列转换为行索引，并创建一个新的DataFrame
frame2 = frame.set_index(['c','d'])
frame2


# In[21]:


# 默认情况下，那些列会从DataFrame中移除，但也可以将其保留下来
frame.set_index(['c','d'],drop=False)


# In[22]:


# reset_index则跟set_index的功能相反
frame2.reset_index()


# In[25]:


# 其它
# 整数索引
# 对于这个系列，使用ser[-1]进行索引会报错
ser = Series(np.arange(3.))
ser


# In[27]:


# 对于非整数索引就没有这样的歧义
ser2 = Series(np.arange(3.),index=['a','b','c'])
ser2[-1]


# In[28]:


# 为了保持良好的一致性，如果你的轴索引含有索引器
# 那么根据整数进行数据选取的操作总是面向标签的
ser.loc[:1]


# In[36]:


# 如果你需要可靠的、不考虑索引类型的、基于位置的索引
# 可以使用Series的iget_value方法和DataFrame的irow和icol方法
ser3 = Series(range(3),index=[-5,1,3])
ser3.get_values()


# In[37]:


frame = DataFrame(np.arange(6).reshape(3,2),index=[2,0,1])
frame


# In[ ]:


# 面板数据（非重点）
# pandas有一个Panel数据结构，其中的每一项都是一个dataframe

