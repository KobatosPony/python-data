
# coding: utf-8

# In[35]:


# 绘图和可视化
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
from matplotlib.font_manager import _rebuild
from datetime import datetime
plt.rcParams['font.sans-serif']='SimHei' #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


# In[22]:


# matplotlib的图像都位于Figure对象中。
fig = plt.figure()
# 不能通过空的figure绘图,必须使用add_subplot创建一个或多个subplot才行
ax1 = fig.add_subplot(2,2,1)  # 代表图像是2x2，选中的是四个subplot中的第一号（编号从1开始）
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)

# 如果这是发出一条绘图命令，matplotlib就会在最后一个用过的subplot
# （如果没有则创建一个）上进行绘制
plt.plot(np.random.randn(50).cumsum(),'k--')  
# k-- 是一个线性选项，用于告诉matplotlib绘制黑色虚线图

# 直接调用add_subplot返回的实例就能在其subplot对象上画图了
_ = ax1.hist(np.random.randn(100),bins=20,color='k',alpha=0.3)
ax2.scatter(np.arange(30),np.arange(30)+3*np.random.randn(30))


# In[23]:


# 更方便的使用plt.subplots
fig,axes = plt.subplots(2,3) # 创建新figure并返回一个含有已创建subplot对象的numpy数组
axes

# pyplot.subplots 的选项
# nrows subplot的行数
# ncols subplot的列数
# sharex 所有subplot应该使用相同的X轴刻度（调节xlim将会影响所有subplot）
# sharey 所有subplot应该使用相同的Y轴刻度（调节xlim将会影响所有subplot）


# In[24]:


# 使用 Figure 的subplots_adjust方法可以修改间距
# subplots_adjust(left=None,buttom=None,right=None,top=None,wspace=None,hspace=None)
fig,axes = plt.subplots(2,2,sharex=True,sharey=True)
for i in range(2):
    for j in range(2):
        axes[i,j].hist(np.random.randn(500),bins=50,color='k',alpha=0.5)
plt.subplots_adjust(wspace=0,hspace=0)


# In[25]:


plt.plot(np.random.randn(30).cumsum(),color='k',linestyle='dashed',marker='o')


# In[27]:


# 进行轴的设置
# 用随机漫步进行演示
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(np.random.randn(1000).cumsum())

# 使用 set_xticks 和 set_xticklabels 可以修改X轴的刻度
ticks = ax.set_xticks([0,250,500,750,1000])

# 通过 set_xticklabels 将任何其他的值用作标签
# 这里旋转了30度并将字体设置为小号
labels = ax.set_xticklabels(['one','two','three','four','five'],rotation=30,fontsize='small')

# 设置标题
ax.set_title("matplotlib plot")

# 注解以及在Subplot上绘图
# text可以将文本绘制在图表的指定坐标（x，y），还可以加上一些自定义格式
# 注意设置 family属性,对应配置文件中的font-family
ax.text(800,10,u"文本",family='sans-serif',fontsize=10)


# In[28]:


# 获取matplotlib 的配置文件路径
print(matplotlib.matplotlib_fname()) 


# In[44]:


#############################################################################
# 完整的简单线形图实例
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# 获取数据
data = pd.read_csv('pydata-book-2nd-edition/examples/spx.csv',index_col=0,parse_dates=True)
spx = data['SPX']

# 绘制基本图
spx.plot(ax=ax,style='k-')

crisis_data = [
    (datetime(2007,10,11),'Peak of bull market'),
    (datetime(2008,3,15),'Bear Stearns Fails'),
    (datetime(2008,9,15),'Lehman Bankruptcy')
]

# 绘制箭头
for date, label in crisis_data:
    ax.annotate(
        label,xy=(date,spx.asof(date)+50),
        xytext=(date,spx.asof(date)+200),
        arrowprops=dict(facecolor='black'),
        horizontalalignment='left',verticalalignment='top'
    )
    
# 放大到 2007-2010
ax.set_xlim(['1/1/2007','1/1/2011'])
ax.set_ylim([600,1800])

ax.set_title('金融危机期间的重要日期',family='sans-serif')

