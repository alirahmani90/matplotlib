from cProfile import label
from turtle import color
from matplotlib import pyplot as plt
from numpy import tile

x=[1,2,3,4,5]
y=[1,2,8,3,9]

x2=[1,2,3,4,5]
y2=[1,3,6,10,8]

plt.plot(x,y,label='line 1',color='#71bfb2')
plt.plot(x2,y2,label='line 2',color='#7eabf2')
plt.title('test')
plt.xlabel('X')
plt.ylabel('Y')

plt.legend()
plt.show()