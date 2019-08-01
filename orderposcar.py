# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 17:02:00 2019

@author: Vacian
"""
fileline=[]
with open ("POSCAR",'r',encoding='UTF-8') as f:
        lines=f.readlines()
        for line in lines:
            fileline.append(line.strip().split())
#order=[3,2,1]
atomnumtypes=fileline[5]           
atomnumbers=fileline[6]
index=8
ordertype=[]
print("Original element order is:")
print(atomnumtypes)
for i in range(0,len(atomnumtypes)):
    ordertype.append(i+1)
print(ordertype)
order=input("Please input you want order:(such as:1 2 3 4)\n")
order=order.split()
for i in range(0,len(order)):
    order[i]=int(order[i])
#print(fileline[index])
orderdir={}
for i in range(0,len(atomnumtypes)):
    orderdir[atomnumtypes[i]]=[]
    for n in range(index,index+int(atomnumbers[i])):
        orderdir[atomnumtypes[i]].append(fileline[n])
    index=index+int(atomnumbers[i])
orderlist=[]
for i in order:
    #print(atomnumtypes[i-1])
    for n in orderdir[atomnumtypes[i-1]]:
        #print(n)
        orderlist.append(n)
atomnumtypeorder=[]
atomnumbersorder=[]
for i in order:
    atomnumtypeorder.append(atomnumtypes[i-1])
    atomnumbersorder.append(atomnumbers[i-1])

for i in range(8,8+len(orderlist)):
    #print(i)
    fileline[i]=orderlist[i-8]
 
fileline[5]=atomnumtypeorder
fileline[6]=atomnumbersorder
print("Output element order is:")
print(fileline[5])
print(order)
with open("POSCAR.vasp",'w') as f:
    for line in fileline:
        f.write(("    ").join(line)+"\n")
