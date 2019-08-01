# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
plt.switch_backend('agg')
filename = 'all'
X,Y1,Y2,Y3,Y4= [],[],[],[],[]
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        value = [float(s) for s in line.split()]
        X.append(value[0])
        Y1.append(value[1])
        Y2.append(value[2])
        Y3.append(value[3])
        Y4.append(value[4])
fig = plt.figure()
ax = plt.subplot(111)
plt.plot(X,Y1,linestyle='solid',label='TDOS')
plt.plot(X,Y2,linestyle='dashed',label='s')
plt.plot(X,Y3,linestyle='dashed',label='p')
plt.plot(X,Y2,linestyle='dashed',label='d')
ax.legend(loc='upper left',prop={'size':24})
ax.spines['left'].set_linewidth(3)
ax.spines['bottom'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)
ax.spines['top'].set_linewidth(3)
ax.set_xlabel('temp',fontsize=24,labelpad = 12.5)
plt.xlabel("Energy/eV",fontsize=24)
plt.ylabel("DOS",fontsize=24)

fig.set_size_inches(18.5, 10.5)
fig.savefig('DOS.png', dpi=200)