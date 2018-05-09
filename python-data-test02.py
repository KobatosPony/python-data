
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


# 数学和统计方法
# sum 对数组中全部或某轴向的元素求和，0长度的数组sum为0
# mean 算术平均数，0长度数组的mean为NaN
# std 、var 分别为标准差和方差，自由度可调（默认为n）
# min 、max 最大值和最小值
# argmin 、 argmax 分别为最大和最小元素的索引
arr = np.random.randn(5,4) # 随机生成正态分布的数据
arr.sum()


# In[3]:


arr.mean()


# In[4]:


# mean和sum这类函数可以接受一个axis参数（用于计算该轴向上的统计值）
# 最终结果会返回一个少一维的数组
arr.mean(axis=1)


# In[5]:


arr


# In[6]:


# cumsum 所有元素的累计和
# cumprod 所有元素的累计积
arr = np.arange(10)
arr


# In[7]:


arr.cumsum()


# In[8]:


arr.cumprod()


# In[9]:


# 对于布尔类型的数组，可以使用sum来计算其中正确的数值
# 布尔类型会被降职转换为0和1
# 布尔类型有特有的方法any 和 all
bools = np.array([False,False,True,False])
bools.any() # 检查是否有True


# In[10]:


bools.all() # 检查是否全为True


# In[11]:


# 这两个方法也可以用于非布尔型数组，非0则代表真


# In[12]:


# 唯一化以及其他的集合逻辑
# np.unique可以找出数组中的唯一值并返回已排序的结果
names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
np.unique(names)


# In[13]:


# np.inld用于测试一个数组的值在另一个数组中的成员资格，返回一个布尔型数组
values = np.array([6,0,0,3,2,5,6])
np.in1d(values,[2,3,6])


# In[14]:


# intersectld(x,y) 计算x，y中的公共元素，并返回有序结果
# unionld（x,y） 计算x和y的并集并返回游戏结果
# setdiffld(x,y) 集合的差，在x中且不在y中
# setxorld(x,y)  集合的对称差，存在于一个数组但不同时存在于两个数组


# In[15]:


# 将数组以二进制格式保存到磁盘
# 使用np.save和np.load 来读写磁盘数组数据，默认情况保存为npy格式的二进制文件中
arr = np.arange(10)
np.save('test_arr',arr)


# In[16]:


np.load('test_arr.npy')


# In[17]:


# np.savez 可以将多个数组保存到一个压缩文件中，将数组以关键字参数形式传入
np.savez('test2_arr',a=arr,b=arr)


# In[18]:


# 读取时会得到一个类似字典的对象
arch = np.load('test2_arr.npz')
arch['a']


# In[19]:


# 线性代数
# diag 以一维数组的形式返回方阵的对角线（或非对角线）元素，或将一维数组转化为方阵
arr = np.arange(25).reshape(5,5)
print(arr)
np.diag(arr)


# In[20]:


# dot 矩阵乘法
# trace 计算对角线元素的和
np.trace(arr)


# In[21]:


# det 计算矩阵行列式
np.linalg.det(arr)


# In[22]:


# eig 计算方阵的本征值和本征向量（特征值和特征向量）
np.linalg.eig(arr)


# In[23]:


# inv 计算方阵的逆
arr = np.random.randn(25)
arr = arr.reshape(5,5)
np.linalg.inv(arr)


# In[24]:


# pinv 计算矩阵的Moore-Penrose伪逆
np.linalg.pinv(arr)


# In[25]:


# qr 计算qr分解
np.linalg.qr(arr)


# In[26]:


# svd 计算奇异值分解
np.linalg.svd(arr)


# In[27]:


# solve 解线性方程组Ax = b，其中A为一个方阵
# 例如：x+2y+z=7;2x-y+3z=7;3x+y+2z=18;这个方程组
# 将未知数的系数写下来，排列成矩阵a
# [[1,2,1],
#[2,-1,3]
#[3,1,2]]
# 常数项构成一个一维数组[7,7,18]
a = np.array([1,2,1,2,-1,3,3,1,2]).reshape(3,3)
print(a)
b = np.array([7,7,18])
np.linalg.solve(a,b)


# In[28]:


# lstsq 计算Ax = b的最小二乘解（看最小二乘法）
np.linalg.lstsq(a,b,rcond='warn')


# In[31]:


# numpy.random 模块对python内置的random进行了补充（重要）
# 使用normal来得到一个标准正态分布的4*4样本数组
samples = np.random.normal(size=(4,4))


# In[32]:


samples


# In[33]:


# seed 确定随机数生成的种子
# permutation 返回一个序列的随机排序或返回一个随机排列的范围
# shuffle 对一个序列就地随机排序
# rand 产生均匀分布的样本值
# randint 从给定的上下限范围内随机选取整数
# randn 产生正态分布（平均值为0，标准差为1）的样本值，类似于MATLAB接口
# binomial 产生二项分布的样本值
# normal 产生正态（高斯）分布的样本值
# beta 产生beta分布的样本值
# chisquare 产生卡方分布的样本值
# gamma 产生Gamma分布的样本值
# uniform 产生在[0,1)中均匀分布的样本值


# In[34]:


# 使用python自带random实现随机漫步
import random


# In[35]:


# 生成1和-1随机出现的数组
position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)


# In[36]:


import matplotlib.pyplot as plt


# In[43]:


plt.title("random walk with +1/-1 steps")
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.plot(walk[:100])


# In[44]:


# 使用np中的random模块
nsteps = 1000
draws = np.random.randint(0,2,size=nsteps)
steps = np.where(draws>0,1,-1)
walk = steps.cumsum()


# In[45]:


walk.min()


# In[46]:


walk.max()


# In[48]:


(np.abs(walk)>=10).argmax()


# In[49]:


# 使用numpy一次模拟多个随机漫步
nwalks = 5000
nsteps = 1000
draws = np.random.randint(0,2,size=(nwalks,nsteps))
steps = np.where(draws>0,1,-1)
walks = steps.cumsum(1)


# In[50]:


walks


# In[55]:


walks.max()


# In[56]:


walks.min()


# In[59]:


# 计算30或-30的最小穿越时间
hits30 = (np.abs(walks)>=30).any(1)
hits30


# In[60]:


hits30.sum()


# In[61]:


# 利用该布尔型数组选出那些穿越的30的随机漫步，并调用argmax在轴1上获取穿越时间
crossing_times = (np.abs(walks[hits30])>=30).argmax(1)
crossing_times.mean()

