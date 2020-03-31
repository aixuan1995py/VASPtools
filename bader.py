# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 00:24:34 2020

@author: Xuan Ai
处理bader电荷运行完之后的ACF.dat文件，把各元素的价电子的数值减去各原子的电荷数，且做平均值输出，并写入bader.dat文件，标准输出为各元素的平均值
"""

import os

r=os.popen("grep ZV POTCAR | awk '{print $6}'")
#os.system("grep ZV POTCAR | awk '{print $6}'")
info = r.readlines()
zval=[]
for line in info:
    line = line.strip()
    zval.append(float(line))
#print(zval)



poslines=[]
with open ("POSCAR",'r',encoding='UTF-8') as f:
        lines=f.readlines()
        for line in lines:
            poslines.append(line.strip().split())
atomnumbers=poslines[6]
elements=poslines[5]
acflines=[]
with open ("ACF.dat",'r',encoding='UTF-8') as f:
        lines=f.readlines()
        for line in lines:
            acflines.append(line.strip().split())

acf=[]
for i in range(2,len(acflines)-4):
#    print(acflines[i])
    acf.append(float(acflines[i][4]))



#zval=[12.0,4.0]



acfdict={}
index=0
for i in range(0,len(elements)):
    acfdict[elements[i]]={}
    acfdict[elements[i]]["number"]=int(atomnumbers[i])
    acfdict[elements[i]]["index"]=index
    acflist=[]
    for x in range(index,index+int(atomnumbers[i])):
        acflist.append(zval[i]-acf[x])
    acfdict[elements[i]]["list"]=acflist
    avg = sum(acflist) / len(acflist)
    acfdict[elements[i]]["avg"]=avg
    index=index+int(atomnumbers[i]) 
    print(elements[i]+"\t"+str(round(avg,3)))

filename = 'bader.dat'
index=0
with open(filename,'w') as f:
    for i in acfdict.keys():    
        for x in range(0,len(acfdict[i]["list"])):
                f.write(str(index+1)+"\t"+i+"\t"+str(round(acfdict[i]["list"][x],3))+"\n")
                index=index+1
    for i in acfdict.keys():
        f.write(i+"\tavg\t"+str(round(acfdict[i]["avg"],3))+"\n")