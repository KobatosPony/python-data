
# coding: utf-8

# In[1]:


from pandas import Series,DataFrame
import pandas as pd
import numpy as np
import sys


# In[2]:


# 数据加载、存储、与文件格式
# 解析函数（用于将文本数据转化为datafrom）
# read_csv 从文件、url、文件型对象中加载带分隔符的数据。默认为逗号
# read_table 从文件、url、文件型对象中加载带分隔符的数据，默认为制表符“\t”
# read_fwf 读取定宽列格式数据（无分隔符）
# read_clipboard 读取剪贴板中的数据，可以看做read_table 的剪贴板版（将网页转化为表格时常用）


# In[3]:


# 使用read_csv将文件读入一个DataFrame
df = pd.read_csv('pydata-book-2nd-edition/examples/ex1.csv')
df


# In[4]:


# 也可以使用read_table,只不过要指定分隔符而已
pd.read_table('pydata-book-2nd-edition/examples/ex1.csv',sep=',')


# In[5]:


# 并不是所有文件都有标题行
# 读入无标题行的文件有两个办法。
# 1.让pandas为其分配默认的列名，也可以自己定制
pd.read_csv('pydata-book-2nd-edition/examples/ex2.csv',header=None)


# In[6]:


pd.read_csv('pydata-book-2nd-edition/examples/ex2.csv',
            names=['a','b','c','d','message'])


# In[7]:


# 如果你希望将message列做成DataFrame的索引，你可以明确表示要将
# 该列放到索引4的位置上，也可以通过index_col参数确定指定的message
names = ['a','b','c','d','message']
pd.read_csv('pydata-book-2nd-edition/examples/ex2.csv',
            names=names,index_col='message')


# In[8]:


# 如果希望将多个列做成一个层次化索引，只需传入由列编号或列名组成的列表即可
parsed = pd.read_csv('pydata-book-2nd-edition/examples/csv_mindex.csv')
parsed


# In[9]:


pd.read_csv('pydata-book-2nd-edition/examples/csv_mindex.csv',index_col=['key1','key2'])


# In[10]:


# 有些表格可能不是用固定的分隔符去分隔字段的（比如空白符或其他模式）
# 对于这种情况，可以编写一个正则表达式来座位read_table的分隔符
list(open('pydata-book-2nd-edition/examples/ex3.txt'))


# In[11]:


# 本例中这个情况可以使用正则表达式\s+来表示
result = pd.read_table('pydata-book-2nd-edition/examples/ex3.txt',sep='\s+')
result


# In[12]:


# 这里，由于列名比数据行的数量少，所以read_table腿短第一列应该是dataframe的索引


# In[13]:


# 解析器函数还有许多参数可以帮助你处理各种各样的异型文件格式
# 比如说，你可以用skiprows跳过文件的第一行、第三行和第四行
pd.read_csv('pydata-book-2nd-edition/examples/ex4.csv')


# In[14]:


pd.read_csv('pydata-book-2nd-edition/examples/ex4.csv',skiprows=[0,2,3])


# In[15]:


# 缺失值处理
pd.read_csv('pydata-book-2nd-edition/examples/ex5.csv')


# In[16]:


# 使用na_values可以接受一组用于表示缺失值的字符串
# 这些字符串在dataframe中会被标记为缺失值
pd.read_csv('pydata-book-2nd-edition/examples/ex5.csv',na_values=['NULL'])


# In[17]:


# 也可以用一个字典为各列指定不同的NA标记值
sentinels = {'message':{'foo','NA'}, 'something':{'two'}}
pd.read_csv('pydata-book-2nd-edition/examples/ex5.csv',na_values=sentinels)


# In[18]:


# nrows 可以指定需要读取的行数（从开始算起）
pd.read_csv('pydata-book-2nd-edition/examples/ex5.csv',na_values=sentinels,nrows=2)


# In[19]:


# 逐块读取文件
# 在处理很大的文件时，或找出大文件中的参数集便于后续处理时，可以逐块对文件进行迭代
result = pd.read_csv('pydata-book-2nd-edition/examples/ex6.csv')
result


# In[20]:


# 逐块读取，需要设置chunksize(行数)
# 还可以使用get_chunk方法，可以使你读取任意大小的块
chunker = pd.read_csv('pydata-book-2nd-edition/examples/ex6.csv',chunksize=1000)
chunker


# In[21]:


# 可以对此对象进行迭代处理
tot = Series([])


# In[22]:


for piece in chunker:
    tot.add(piece['key'].value_counts(),fill_value=0)
tot


# In[23]:


# 将数据写入到文本格式
data = pd.read_csv('pydata-book-2nd-edition/examples/ex5.csv')
data


# In[24]:


# 使用DataFrame的to_csv方法，可以将数据写到一个以逗号分隔的文件中
data.to_csv('pydata-book-2nd-edition/examples/ex6_out.csv')


# In[25]:


# 当然还可以使用其它分隔符（这里直接写出到sys.stdout，所以只是会打印）
data.to_csv(sys.stdout,sep='|')


# In[26]:


# 缺失值在输出结果中会被表示为空字符串。你可以希望将其表示为别的标记值
data.to_csv(sys.stdout,na_rep='NULL')


# In[27]:


# 如果没有设置其它选项，则会写出行和列的标签，当然可以用hander禁用
data.to_csv(sys.stdout,header=False)


# In[28]:


# 还可以只写出一部分的列，并以你指定的顺序排列
data.to_csv(sys.stdout,index=False)


# In[29]:


# Series也有一个to_csv方法
dates = pd.date_range('1/1/2000',periods=7)
ts = Series(np.arange(7),index=dates)
ts


# In[30]:


ts.to_csv('pydata-book-2nd-edition/examples/tseries.csv')
ts.to_csv(sys.stdout)


# In[34]:


# 虽然只需一点整理工作（无header行，第一列作索引）
Series.from_csv('pydata-book-2nd-edition/examples/tseries.csv',parse_dates=True)

