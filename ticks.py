import matplotlib.pyplot as plt
import numpy as np

'''
2.7 tick能见度
'''

x = np.linspace(-3,3,50)
y = 0.1*x

plt.figure()
plt.plot(x,y,linewidth=10)
plt.ylim(-2,2)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

'''
改变ticks的字体大小
'''
for label in ax.get_xticklabels() +ax.get_yticklabels():
    # 设置字体大小
    label.set_fontsize(12)
    # 每一个tick外面都有一个box，设置该box的background color,alpha 为透明度
    label.set_bbox(dict(facecolor='white',edgecolor='None',alpha=0.7))

plt.show()
