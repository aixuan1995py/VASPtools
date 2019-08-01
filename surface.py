# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 20:50:46 2018

@author: Vacian
"""


fileline=[]
with open ("out",'r',encoding='UTF-8') as f:
        lines=f.readlines()
        for line in lines:
            fileline.append(line.strip().split())
zze=[]
for i in range(0,len(fileline)):
    zze.append(round(float(fileline[i][1]),4))
e=[]
for i in range(0,len(fileline)):
    e.append(round(float(fileline[i][2]),4))
    
bulk=round(float(fileline[0][3]),4)
area=round(float(fileline[0][4]),4)
num=int(fileline[0][5])
eout=[]
for i in range(0,len(e)):
    eout.append((e[i]-num*bulk)/(2*area))
zzeout=[]
for i in range(0,len(zze)):
    zzeout.append((zze[i]-num*bulk)/(area))
out=[]
for i in range(0,len(zze)):
    out.append((zzeout[i]-eout[i])*16.21)

for i in range(0,len(out)):
    print(round(out[i],3))