
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from io import StringIO,BytesIO
from pandas import Series,DataFrame


# In[2]:


plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False


# In[3]:


# 图形的绘制
# matplotlib 中有一些表示常见图形的对象。这些对象被称为patch
# 其中有些可以再pyplot中找到，完整集合位于matplotlib.patches
# 要添加图形，需要先创建块对象shp，然后通过ax.add_patch(shp)添加到subplot中
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# 添加矩形
rect = plt.Rectangle((0.2,0.75),0.4,0.15,color='k',alpha=0.3,angle=1)
ax.add_patch(rect)

# 添加圆形
circ = plt.Circle((0.7,0.2),0.15,color='b',alpha=0.3)
ax.add_patch(circ)

# 添加三角形
pgon = plt.Polygon([[0.15,0.15],[0.35,0.4],[0.2,0.6]],color='g',alpha=0.5)
ax.add_patch(pgon)


# In[4]:


# 将图表保存到文件,dpi为图像分辨率（每英寸点数）,默认为100
fig.savefig('figpath.png',dpi=400)


# In[5]:


# 并非要写入磁盘，也可写入任何文件类型的对象
# string 类型用StringIO，byte类型用bytesio
buffer = BytesIO()
fig.savefig(buffer)
plot_data = buffer.getvalue()


# In[6]:


# pandas中的绘图函数
# pandas能够直接根据其数据类型来绘制图表
# Series和DataFrame都有一个用于生成各类图表的plot方法，默认情况下，生成的是线形图
s = Series(np.random.randn(10).cumsum(),index=np.arange(0,100,10))
print(s)
# 有ax参数可以指定绘制的subplot对象，没有则使用默认
s.plot()


# In[7]:


# dataframe的plot方法会在一个subplot中为各列绘制一条线，并自动创建图例
df = DataFrame(np.random.randn(10,4).cumsum(0),
              columns=['A','B','C','D'],
              index=np.arange(0,100,10))
df.plot(grid=True)


# In[8]:


# 柱状图
# kind='bar'或kind='barh'生成垂直或水平柱状图
# Series和DataFrame的索引将会被用作刻度


# In[9]:


fig, axes = plt.subplots(2,1)
data = Series(np.random.rand(16),index=list('abcdefghijklmnop'))
data.plot(kind='bar',ax=axes[0],color='k',alpha=0.7)
data.plot(kind='barh',ax=axes[1],color='k',alpha=0.7)


# In[16]:


tips = pd.read_csv('pydata-book-2nd-edition/examples/tips.csv')
party_counts = pd.crosstab(tips.day,tips.size)
party_counts


# In[ ]:


# 直方图和密度图

