
# coding: utf-8

# In[16]:


# 导入pandas
from pandas import Series, DataFrame
import pandas as pd
import numpy as np


# In[17]:


# Series是一种类似于一维数组的对象，它由一组数据以及一组与之相关的数据标签（索引）组成
obj = Series([4,7,-5,3])
obj
# 索引在左，值在右


# In[18]:


# 可以通过values和index属性获取其数组表现形式和索引对象
obj.values


# In[19]:


obj.index


# In[20]:


# 使用自定义索引创建Series
obj2 = Series([4,7,-5,3], index=['d','b','a','c'])
obj2


# In[21]:


obj2.index


# In[12]:


# 通过索引获取单个或一组值
obj2['a']


# In[13]:


obj2['b']


# In[14]:


obj2[['c','a','d']]


# In[15]:


# 使用基于numpy的数组运算都会保留索引和值之间的链接
obj2 * 2


# In[22]:


np.exp(obj2)


# In[23]:


# Series 可以看成是一个定长的有序字典，可以用在许多原本需要字典参数的函数中
'b' in obj2


# In[24]:


'e' in obj2


# In[25]:


# 可以通过字典来创建Series
# 索引就是原字典的键（只传入一个字典的情况下）
sdata = {'Ohio':35000,'Texas':71000,'Oregon':16000,'Utah':5000}
obj3 = Series(sdata)
obj3


# In[26]:


# 如果传入另一个字典作为键，那么pandas将把找不到索引的值设为NaN
states = ['California','Ohio','Oregon','Texas']
obj4 = Series(sdata, index=states)
obj4


# In[27]:


# 可以通过实例方法来判断
obj4.isnull()


# In[28]:


# Series在算术运算中会自动对齐不同索引的数据
obj3


# In[29]:


obj4


# In[30]:


obj3 + obj4


# In[32]:


# Series对象本身及其索引都有一个name属性（重要）
obj4.name = 'population'


# In[33]:


obj4.index.name = 'state'


# In[34]:


obj4


# In[35]:


# DataFrame是一个表格型的数据结构，既有行索引也有列索引
# 构建DataFrame的方法
# 直接传入一个由登场列表或numpy数组组成的字典
data = {
    'state':['Ohio','Ohio','Ohio','Neveda','Neveda'],
    'year':[2000,2001,2002,2001,2002],
    'pop':[1.5,1.7,3.6,2.4,2.9]
}
frame = DataFrame(data)
frame


# In[38]:


# 结果dataframe会自动加上索引，且全部列会被有序排列
# 如果指定了列序列，则dataframe的列会按照指定顺序排列
DataFrame(data, columns=['year','state','pop'])


# In[39]:


# 如果传入的列在数据中找不到就会产生NA值
frame2 = DataFrame(data,columns=['year','state','pop','dept'],
                   index=['one','two','three','four','five'])


# In[40]:


frame2


# In[41]:


frame2.columns


# In[43]:


# 通过类似字典的方式可将dataframe的列获取为一个series
frame2['state']


# In[44]:


frame2.year


# In[45]:


# 列可以通过赋值进行修改
frame2['dept'] = 16.5


# In[46]:


frame2


# In[47]:


# 将列表或数组赋值给某个列时，其长度必须跟dataframe长度匹配
# 如果赋值的是一个series，就会精确匹配dataframe的索引
val = Series([-1.2,-1.5,-1.8],index=['two','four','five'])
frame2.dept = val
frame2


# In[48]:


# dataframe也可以进行转置
frame2.T


# In[49]:


# values,index,和column
frame2.columns


# In[50]:


frame2.index


# In[51]:


frame2.values


# In[52]:


# 也可以给column和index设置name属性
frame2.columns.name = 'state'
frame2.index.name = 'year'
frame2


# In[53]:


# 索引的index对象时不可修改的
index = pd.Index(np.arange(3))


# In[54]:


index


# In[56]:


# index对象的特有方法
# is_monotonic 当各元素均大于等于前一个元素时，返回True
# is_unique 当index没有重复值时，返回true
# unique 计算index中唯一值的数组


# In[59]:


# 重新索引
# 使用reindex方法将会根据新索引进行重排
obj


# In[60]:


obj2 = obj.reindex([0,1,2,3,4])
obj2


# In[61]:


# 自定义缺失值
obj.reindex([0,1,2,3,4,5],fill_value=0)


# In[62]:


# 使用method可以定义缺失值的填充方式
obj3 = Series(['blue','purple','yello'],index=[0,2,4])
# ffill或pad 前向填充
# bfill或backfill 后向填充
obj3.reindex(range(6),method='ffill')


# In[64]:


# 可以使用ix更简洁的进行重新索引
frame = DataFrame(np.arange(9).reshape((3,3)),index=['a','c','d'],
                    columns=['Ohio','Texas','California'])
frame


# In[69]:


states = ['Texas','Utah','California']
frame.ix[['a','b','c','d'],states]


# In[70]:


# 丢弃指定轴上的项
# drop方法会返回一个删除了指定轴的对象
obj = Series(np.arange(5.),index=['a','b','c','d','e'])
new_obj = obj.drop('c')
new_obj


# In[71]:


# 对于dataframe，可以删除任意轴上的索引值
data = DataFrame(np.arange(16).reshape((4,4)),
                index=['Ohio','Colorado','Utah','New York'],
                columns=['one','two','three','four'])


# In[72]:


data


# In[73]:


data.drop('two',axis=1)


# In[74]:


data.drop('Ohio')


# In[75]:


# 索引、选取和过滤
# Series 的索引和numpy数组类似，只是不只是整数
obj = Series(np.arange(4.),index=['a','b','c','d'])
obj


# In[76]:


obj['b']


# In[77]:


obj[1]


# In[78]:


obj[obj<2]


# In[79]:


# 切片运算和python切片不同，末端是包含的
obj['a':'b']


# In[80]:


# dataframe索引
data = DataFrame(np.arange(16).reshape((4,4)),
                 index=['Ohio','Colorado','Utah','New York'],
                columns=['one','two','three','four'])
data


# In[81]:


data['two']


# In[86]:


data[['three','one']]


# In[90]:


# 还可以通过切片或布尔型数组选取行
data[:2]


# In[91]:


data[data['three']>5]


# In[92]:


# 通过布尔型dataframe进行索引
data < 5


# In[93]:


data[data<5] = 0


# In[94]:


data


# In[101]:


data.get_values()


# In[107]:


data.loc['Ohio']


# In[108]:


# 算术运算和数据对齐
# pandas最重要的一个功能是，它可以对不同索引的对象进行算术运算
# 在将对象相加是，如果存在不同的索引对，则结果的索引就是该索引对的并集
s1 = Series([7.3,-2.5,3.4,1.5],index=['a','c','d','e'])
s2 = Series([-2.1,3.6,-1.5,4,3.4],index=['a','c','e','f','g'])
s1


# In[109]:


s2


# In[110]:


s1 + s2


# In[117]:


# 对于dataframe，对齐操作会同时发生在行和列上
df1 = DataFrame(np.arange(9.).reshape((3,3)),columns=list('bcd'),
               index=['Ohio','Texas','Colorado'])
df2 = DataFrame(np.arange(12.).reshape((4,3)),columns=list('bde'),
               index=['Utah','Ohio','Texas','Oregon'])
df1


# In[118]:


df2


# In[119]:


df1 + df2


# In[126]:


# 使用DataFrame对象的add方法可以对NA值进行填充（第二个参数）
# add +; sub -; div /; mul *
df1.add(df2,fill_value=0)

