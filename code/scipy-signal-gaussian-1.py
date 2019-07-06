import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_excel('3c446.xlsx')
start_time1 = data['time']
fluence1 = data['flux']
start_time2=[]
for i in range(0,len(start_time1),7):
    time=start_time1[i]
    start_time2=np.append(start_time2,time)                             #七个一组平分横坐标时间轴
juanjihe=[0.006,0.061,0.242,0.383,0.242,0.061,0.006]                    #一维数据高斯平滑卷积核（3倍标准差）
new2=[]
j=0
s=0
for i in range(0,len(fluence1),7):
    new=[]
    for j in range(7):
        new_data=juanjihe[j]*fluence1[i]
        j=j+1
        i=i+1
        new=np.append(new,new_data)
    new1=np.sum(new)
    new2=np.append(new2,new1)                                          #数据七个分一组，分别与七个卷积核做卷积
plt.figure(figsize=(20,10))
plt.plot(start_time1,np.log10(fluence1),label='3c446',linewidth=0.8,color='r')
plt.plot(start_time2,np.log10(new2),label='Gauss_3c446',linewidth=1,color='blue')
plt.xlabel('time[day]')
plt.ylabel('log10_gaussfluence[erg s$^{-1}$ cm$^{-2}$]')
plt.title('3c446 Gauss-Flat Light Curve')
plt.legend(loc='best')
plt.show()
