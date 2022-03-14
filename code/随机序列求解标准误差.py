
from statistics import mean
import numpy as np
import random as ra



def yingying(step,seed,num,max):
    #step: 实验次数(n)
    #seed：数据基数
    #num:  数据个数
    #max： 数据波动的最大值
    
    data = []

    for i in range(num):
        point = seed + ra.uniform(0,max)
        data.append(point)

    #得到第一组数据本身的误差值
    print(data[0:10])
    std_self = np.std(data[0:step])

    std_cube= []

    j = 0
    while j < (len(data)):
        mean = np.mean(data[j:j + step])
        std_cube.append(mean)
        j = j + step
    #print(std_cube)    
    

    return(std_self,np.std(std_cube))



y1 = []
y2 = []
for k in range(50):
    a1 = yingying(step=225,seed=1000,num=10000,max=30)[0]
    y1.append(a1)

    a2 = yingying(step=225,seed=1000,num=10000,max=30)[1]
    y2.append(a2)
print(mean(y1),mean(y2))

x = np.array(list(range(1,51)))
import matplotlib.pyplot as plt

plt.plot(x,y1,label='STD')
plt.plot(x,y2,label='SEM')
plt.legend()
plt.title('The comparison of STD and SEM (n=225)')
plt.show()

        
        
        


