
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


# 创建numpy数组
data1 = [6.,7.5,8.,0.,1.]


# In[4]:


arr1 = np.array(data1)


# In[5]:


arr1


# In[6]:


# 嵌套序列将会被转换为一个多维数组
data2 = [[1,2,3,4],[5,6,7,8]]


# In[7]:


arr2 = np.array(data2)


# In[8]:


arr2


# In[9]:


# 数组的秩
arr2.ndim


# In[10]:


# 数组的维度
arr2.shape


# In[11]:


# 除非显式说明。np.array会尝试为新建的这个数组推断出一个较为合适的数据类型。
# 数据类型保存在一个特殊的dtype对象中。
arr1.dtype


# In[12]:


arr2.dtype


# In[13]:


# 除了np.array，还有一些函数也可以新建数组。比如
# zeros和ones分别可以创建指定长度或形状的全0或全1数组
# empty可以创建一个没有任何具体值的数组
# 使用这些方法创建时只需传入一个表示形状的元祖即可
np.zeros(10)


# In[14]:


np.zeros((3,6))


# In[15]:


np.empty((2,3,2))


# In[16]:


# arange是python内置函数range的数组版
np.arange(15)


# In[18]:


# 创建一个正方的N * N单位矩阵（对角线为1，其余为0）
np.eye(10)
np.identity(4)


# In[19]:


# 使用astype显式转换其dtype (如果出错会应发TypeError)
# 使用astype无论如何都会创建出一个新的数组
arr = np.array([1,2,3,4,5])


# In[20]:


arr.dtype


# In[21]:


float_arr = arr.astype(np.float64)
float_arr.dtype


# In[22]:


# 数组的简单运算
arr = np.array([[1.,2.,3.],[4.,5.,6.]])
arr


# In[23]:


arr * arr


# In[24]:


arr - arr


# In[25]:


arr + arr


# In[26]:


# 基本的索引和切片
arr = np.arange(10)
arr


# In[27]:


arr[5]


# In[28]:


arr[5:8]


# In[29]:


# 当你将一个标量赋值给一个切片时，该值会自动传播到整个选区
arr[5:9] = 12


# In[30]:


arr


# In[31]:


arr_slice = arr[5:8]
arr_slice


# In[32]:


arr_slice[1]


# In[33]:


# 二维数组的索引方式
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2d[2]


# In[34]:


# 以下两种方式等价
arr2d[0][2]


# In[35]:


arr2d[0,2]


# In[36]:


# 三维数组
arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
arr3d


# In[37]:


arr3d[0]  # 会返回一个2 * 3的数组


# In[38]:


# 标量和数组都可以被赋值给arr3d[0]
old_value = arr3d[0].copy()


# In[39]:


arr3d[0] = 42


# In[40]:


arr3d


# In[41]:


arr3d[0] = old_value


# In[42]:


arr3d


# In[43]:


arr3d[1,0]


# In[45]:


# 使用random中的randn函数生成一些正态分布的随机数据
names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
data = np.random.randn(7,4)


# In[46]:


names


# In[47]:


data


# In[48]:


# 堆names和字符串‘Bob’的比较运算将会产生一个布尔型数组
names == 'Bob'


# In[49]:


# 这个布尔型数组可用于数组索引
data[names == 'Bob']


# In[50]:


# 还可以混合使用
data[names == 'Bob', 3]


# In[51]:


data[names == 'Bob', 2:]


# In[54]:


# 要选择除Bob外其它值，可以使用！=或者负号对条件进行否定
# 也可以使用 &（和）、|（或之类的布尔运算符）
names != 'Bob'


# In[55]:


# 花式索引
# 先创建一个数组
arr = np.empty((8,4))
for i in range(8):
    arr[i] = i


# In[56]:


arr


# In[57]:


# 传入一个用于指定顺序的整数列表或ndarray即可以特定顺序选取行子集
arr[[4,3,0,6]]  # 选取第四行，三行， 零行和六行


# In[58]:


# 使用负数将会从末尾开始索引
arr[[-3,-5,-7]]


# In[59]:


# 传入多个索引数组
arr = np.arange(32).reshape((8,4))
arr


# In[60]:


arr[[1,5,7,2],[0,3,1,2]]
# 最终会选出（1,0）（5,3）（7,1）（2,2）


# In[61]:


# 如果要选取矩阵的行列子集要使用
arr[[1,5,7,2]][:,[0,3,1,2]]


# In[63]:


# 也可以使用np.ix_函数，它可以将两个一位数组转化为选取方形区域的索引器
arr[np.ix_([1,5,7,2],[0,3,1,2])]


# In[64]:


# 数组转置（矩阵的转置）
arr = np.arange(15).reshape((3,5))


# In[65]:


arr


# In[66]:


arr.T


# In[68]:


# 使用dot函数计算矩阵乘法
arr = np.random.randn(6,3)
np.dot(arr.T, arr)


# In[70]:


# 使用transpose也可以对矩阵进行转置，需要提供一个由轴编号组成的元祖
# 该元祖指定了转置的轴对象
arr = np.arange(16).reshape((2,2,4))
arr


# In[72]:


arr.transpose((1,0,2))
# 此例中，1,0,2表示轴的转换方式，shape为（2，2，4）
# 先给原shape编号（2[0],2[1],4[2]）
# 按照所给元祖转换为（2[1],2[0],4[2]）
# 其中元素也按照如此变化
# 比如8的索引为[1][0][2],则改变为[0][1][2]
# 所有元素按此规则改变最终得到结果


# In[73]:


# 利用数组进行数据处理
points = np.arange(-5,5,0.01) # 1000个间隔相等的点
points


# In[74]:


# np.meshgrid 函数接受两个一维数组并产生两个二位矩阵（对应两个数组中的x，y对）
xs, ys = np.meshgrid(points, points)


# In[75]:


xs


# In[76]:


ys


# In[77]:


import matplotlib.pyplot as plt


# In[78]:


z = np.sqrt(xs**2 + ys**2)


# In[79]:


z


# In[83]:


# 使用pylot进行绘图
plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2+y^2}$ for a grid of values")

