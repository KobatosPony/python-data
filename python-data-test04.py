
# coding: utf-8

# In[6]:


from pandas import DataFrame,Series
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Dataframe和Series之间的运算


# In[7]:


# 先尝试计算二维数组与某行之间的差
arr = np.arange(12.).reshape((3,4))
arr


# In[8]:


arr[0]


# In[9]:


arr - arr[0]
# 这叫做广播
# DataFrame和Series之间的运算差不多也是如此


# In[10]:


frame = DataFrame(np.arange(12.).reshape((4,3)),columns=list('bed'),
                 index=['Utah','Ohio','Texas','Oregon'])


# In[12]:


series = frame.iloc[0]


# In[13]:


frame


# In[14]:


series


# In[15]:


frame - series


# In[16]:


# 默认情况下，dataframe 和 series之间的算术运算会将series索引匹配到
# dataframe的列，然后沿着行一直向下传播
# 如果某个索引在dataframe的列或series的索引中找不到
# 则参与运算的两个对象就会被重新索引并形成并集
series2 = Series(np.arange(3),index=['b','e','f'])
frame + series2


# In[17]:


# 如果你希望匹配行并在列上广播，则必须使用算术运算方法
series3 = frame['d']
series3


# In[18]:


# 传入的轴号就是需要匹配的轴
frame.sub(series3,axis=0)


# In[23]:


# 函数应用和映射
# numpy的ufuncs（元素级数组方法）也可用于操作pandas对象
frame = DataFrame(np.random.randn(4,3),columns=list('bde'),
                 index=['Utah','Ohio','Texas','Oregon'])
frame


# In[27]:


np.abs(frame)


# In[28]:


print(frame)
# 另一个常见的操作是，将函数应用到由各列或行所形成的一维数组上
# dataframe的apply方法即可实现此功能
f = lambda x:x.max() - x.min()
frame.apply(f)


# In[29]:


frame.apply(f,axis=1)


# In[31]:


# 许多常见的数组统计功能会被实现成dataframe的方法（如sum和mean）
# 除标量值外，传递给apply的函数还可以返回由多个值组成的series
def f(x):
    return Series([x.min(),x.max()],index=['min','max'])
frame.apply(f)


# In[32]:


frame.apply(f,axis=1)


# In[33]:


# 此外，元素级的python函数也是可以用的。
# 假如你想得到frame中各个浮点值的格式化字符串，可以会用applymap
format = lambda x:'%.2f' % x
frame.applymap(format)


# In[35]:


# 之所以叫做applymap，是因为series有一个用于应用元素级函数的map方法
frame['e'].map(format)


# In[36]:


# 排序和排名
# 使用sort_index方法会返回一个基于行或列索引排序的新对象
obj  = Series(range(4),index=list('dabc'))
obj.sort_index()


# In[37]:


# 而对于dataframe，则可以根据任意一个轴上的索引进行排序
frame = DataFrame(np.arange(8).reshape((2,4)),index=['three','one'],
                 columns=list('dabc'))
frame.sort_index()


# In[38]:


frame.sort_index(axis=1)


# In[39]:


# 默认是按照升序，也可以按照降序
frame.sort_index(axis=1,ascending=False)


# In[41]:


# 若要按值对series进行排序，可使用其order方法 ,新版本中并没有这个方法
# 在排序时，任何确实值默认都会被放到series末尾
obj = Series([4,np.NAN,7,np.NAN,-3,2])


# In[44]:


obj.sort_values() # 新版中使用sort_values实现


# In[47]:


# 在dataframe上，你可能希望根据一个或多个列中的值进行排序。
# 将一个或多个列的名字传递给by选项即可达到该目的
frame = DataFrame({'b':[4,7,-3,2],'a':[0,1,0,1]})
frame


# In[49]:


frame.sort_values(by='b')


# In[50]:


# 要根据多个列进行排序，传入名称的列表即可
frame.sort_values(by=['a','b'])


# In[56]:


# ranking跟排序关系密切，且它会增设一个排名值（从1开始，一直到数组中有效数据的数量）
# 它跟numpy.argsort产生的简洁排序索引差不多，只不过它可以根据某种规则破坏平级关系
# 默认情况下，rank是通过“为各组分配一个平均排名”的方式破坏平级关系的
# argsort会将数组从小到大排列并提取索引
arr1 = np.array([5,3,6,4,1,2,4])
np.argsort(arr1)


# In[57]:


obj = Series([7,-5,7,4,2,0,4])
obj.rank()


# In[58]:


# 也可以根据值在元数据中出现的顺序给出排名
obj.rank(method='first')


# In[59]:


# 按照降序进行排名
obj.rank(ascending=False,method='max')


# In[60]:


# 排名时用于破坏平级关系的method选项
# average 默认，在相等分组中，为各个值分配平均排名
# min 使用整个分组的最小排名
# max 使用整个分组的最大排名
# first 按值在原始数据中出现顺序分配排名


# In[61]:


# 带有重复值的轴索引
obj = Series(range(5),index=list('aabbc'))
obj


# In[63]:


# is_unique属性可以告诉你它的值是否是唯一的
obj.index.is_unique


# In[64]:


# 对于带有重复值的索引，如果选取则会返回一个series
# 对应单个值则会返回标量值
obj['a']


# In[65]:


# dataframe也是如此
df = DataFrame(np.random.randn(4,3),index=['a','a','b','b'])
df


# In[68]:


df.loc['b']


# In[69]:


# 汇总和计算描述统计
df = DataFrame([[1.4,np.NAN],[7.1,-4.5],[np.NAN,np.NAN],[0.75,-1.3]],
              index=list('abcd'),columns=['one','two'])


# In[70]:


df


# In[71]:


# 调用sum方法将会返回一个含有列小计的series
df.sum()


# In[72]:


# 传入axis=1将会按行进行求和运算
df.sum(axis=1)


# In[73]:


# 其中的nan值会自动被排除，除非整个切片都是nan，通过skipna选项可以禁用该功能
df.mean(skipna=False,axis=1)


# In[74]:


# 间接统计（idxmin，idxmax）返回的是间接统计（达到最小值或最大值的索引）
df.idxmax()


# In[75]:


df.idxmin()


# In[76]:


# 另一些方法则是累计型的
# 前一列的计算结果会累计到后一次
df.cumsum()


# In[77]:


# 有的方法既不是约简型也不是累计型。
# 比如describe，它用于一次性产生多个汇总统计
df.describe()


# In[78]:


# 对于非数值型数据，describe会产生另外一种汇总统计
obj = Series(['a','a','b','c']*4)
obj.describe()


# In[ ]:


# 方法
# count 非NA值的数量
# describe 真毒Series或各DateFrame列计算汇总统计
# min、max 计算最小值和最大值
# quantile 计算样本的分位数（0到1）
# var 样本值的方差
# std 样本值的标准差
# skew 样本值的偏度（三阶矩）
# kurt 样本值的峰度（四阶矩）
# cumprod 样本值的累积积
# diff 计算一阶差分
# pct_change 计算百分数变化

