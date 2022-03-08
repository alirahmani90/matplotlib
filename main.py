from cProfile import label
from matplotlib import pyplot as plt

slises = [200, 60, 100]
labels=['city','jungle','farm']
colors = ['#3397b0','#33b054','#ede61a']
plt.pie(slises,labels=labels,colors=colors,autopct='%1.1f%%',explode=(0,0.1,0),shadow=True)
plt.title('test')


# plt.legend()
plt.show()
