from matplotlib import pyplot as plt
import random

ages=[]
for num in range(101):
    ages.append(random.randint(1,120))

bins=[10,20,30,40,50,60,70,80,90,100,130]
plt.hist(ages,bins,rwidth=0.9,color='pink',label='ages')
# plt.plot(x2,y2,label='line 2',color='#7eabf2')
plt.title('test')
plt.xlabel('ages')
plt.ylabel('Y')

plt.legend()
plt.show()