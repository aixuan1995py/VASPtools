# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 09:47:53 2019

@author: Vacian
"""

import numpy as np

#读取DOSCAR
doslines=[]
with open ("DOSCAR",'r',encoding='UTF-8') as f:
        lines=f.readlines()
        for line in lines:
            doslines.append(line.strip().split())
#读取POSCAR
poslines=[]
with open ("POSCAR",'r',encoding='UTF-8') as f:
        lines=f.readlines()
        for line in lines:
            poslines.append(line.strip().split())
#读取元素种类
elements=poslines[5]
#读取元素个数
atomnumbers=poslines[6]
#建立某原子绝对位置
atomnumber={}
a=0
b=0
for i in range(0,len(elements)):
    b=a+1
    a=a+int(atomnumbers[i])
    atomnumber[str(elements[i])]=list(range(b,a+1))
#DOSCAR处理
index = 0
#原子数
natoms = int(doslines[index][0])
index = 5
#点数
nedos = int(doslines[index][2])
#费米能级
efermi = float(doslines[index][3])
print(natoms,nedos,efermi,elements,atomnumbers)
#TDOS列表
tdosx=[]
tdosy=[]
for i in range (0,nedos):
    index=index+1
    tdosx.append(float(doslines[index][0])-efermi)
    tdosy.append(float(doslines[index][1]))
#print(index)
#PDOS字典
obits=['s','py','pz','px','dxy','dyz','dz2','dxz','dx2']
pdos={}
for i in range(0,len(elements)):
    #print(elements[i])
    pdos[str(elements[i])]={}
    for x in range(0,int(atomnumbers[i])):
        pdos[str(elements[i])][str(x)]={}
        pdos[str(elements[i])][str(x)]['x']=[]
        pdos[str(elements[i])][str(x)]['p']=[]
        pdos[str(elements[i])][str(x)]['d']=[]
        for s in obits:
            pdos[str(elements[i])][str(x)][s]=[]
        index=index+1
        for n in range (0,nedos):
            index=index+1
            for s in range(0,len(obits)):
                pdos[str(elements[i])][str(x)][obits[s]].append(float(doslines[index][s+1]))
            pdos[str(elements[i])][str(x)]['x'].append(float(doslines[index][0])-efermi)
            pdos[str(elements[i])][str(x)]['p'].append(float(doslines[index][2])+float(doslines[index][3])+float(doslines[index][4]))
            pdos[str(elements[i])][str(x)]['d'].append(float(doslines[index][5])+float(doslines[index][6])+float(doslines[index][7])+float(doslines[index][8])+float(doslines[index][9]))    
        #print(index)
#PDOS各轨道加和字典     
tpdos={}
for i in range(0,len(elements)):
    #print(elements[i])
    tpdos[str(elements[i])]={}
    tpdos[str(elements[i])]['s']=np.zeros(nedos)
    tpdos[str(elements[i])]['p']=np.zeros(nedos)
    tpdos[str(elements[i])]['d']=np.zeros(nedos)
    for x in range(0,int(atomnumbers[i])):
        tpdos[str(elements[i])]['s']=np.array(pdos[str(elements[i])][str(x)]['s'])+tpdos[str(elements[i])]['s']
        tpdos[str(elements[i])]['p']=np.array(pdos[str(elements[i])][str(x)]['p'])+tpdos[str(elements[i])]['p']
        tpdos[str(elements[i])]['d']=np.array(pdos[str(elements[i])][str(x)]['d'])+tpdos[str(elements[i])]['d']
#文件输出
filename = 'tpdos.dat'
with open(filename,'w') as f:
    for i in range(0,len(elements)):
        f.write(elements[i]+"\n")
        f.write("x\ts\tp\td\n")
        for x in range(0,nedos):
            f.write(str(format(float(tdosx[x]),'15.8f')).ljust(15)+str(format(float(tpdos[elements[i]]['s'][x]),'15.8f')).ljust(15)+str(format(float(tpdos[elements[i]]['p'][x]),'15.8f')).ljust(15)+str(format(float(tpdos[elements[i]]['d'][x]),'15.8f')).ljust(15)+"\n")
#自定原子位置选择
dmetal=elements
obitcentre=["d","s","p"]

slect='1-24'
if "-" in slect:
    if "," not in slect:
        slects=slect.split("-")
        slectss=[]
        if len(slects) == 2:
            for i in range(int(slects[0]),int(slects[1])+1):
                slectss.append(str(i))
            slects=slectss
        else:
            print("Error!")
    else:
        slects=slect.split(",")
        slectss=[]
        for i in range(0,len(slects)):
            if "-" in slects[i]:
                slectsss=slects[i].split("-")
                if len(slectsss) == 2:
                    for q in range(int(slectsss[0]),int(slectsss[1])+1):
                        slectss.append(str(q))
            else:
                slectss.append(slects[i])
        slects=slectss
elif "," in slect:
    slects=slect.split(",")
    
else:
    slects=slects=slect.split()


for i in range(0,len(slects)):
    slects[i]=int(slects[i])

slects=set(slects)
#print(slects)
slecetdict={}
for key,value in atomnumber.items():
    for a in slects:
        if a in value:
            slecetdict[a]=key          
#print(slecetdict)
a=slecetdict.values()
a=set(a)
a=list(a)
#print(a)
c={}
for i in range(0,len(a)):
    c[a[i]]=[]
    for b,d in slecetdict.items():
        if str(d) == a[i]:
            c[a[i]].append(b)

#绝对位置转化为相对位置
p={}
for i in c.keys():
    p[i]=[]
    for e in c[i]:
        p[i].append(atomnumber[i].index(e)+1)
        
            
print("The all band center!")
#全部原子的各带中心   
for i in dmetal:
    for n in obitcentre:
        x=np.array(tdosx)
        y=np.array(tpdos[i][n])
        for q in range(0,len(x)):
            if x[q] > 0:
                fer=q
                break
        x0=x[0:int(fer)]
        y0=y[0:int(fer)]
        inte_a0=np.trapz(y0,x0)
        xy=x*y
        inte_a=np.trapz(y,x)
        inte_b=np.trapz(xy,x)
        if float(inte_a) < 0.0001:
            onecenter="Null"
            tocenter="Null"
        else:
            onecenter=inte_b/inte_a
            z = np.linspace(float(onecenter),float(onecenter),nedos)
            zy= x-z
            zy2= y*zy*zy
            int_c= np.trapz(zy2,x)
            tocenter=int_c/inte_a
            onecenter=round(onecenter,3)
            tocenter=round(tocenter,3)
        print(str(i)+"\t"+str(n)+" fill is\t"+ str(round(inte_a0,3))+"\tOne center\t"+str(onecenter)+"\tTwo center\t"+str(tocenter))

print("The slect atoms band center!")
print(c)
#PDOS各轨道加和字典     
ppdos={}
for i in p.keys():
    ppdos[str(i)]={}
    ppdos[str(i)]['s']=np.zeros(nedos)
    ppdos[str(i)]['p']=np.zeros(nedos)
    ppdos[str(i)]['d']=np.zeros(nedos)
    for x in range(0,len(p[i])):
        ppdos[str(i)]['s']=np.array(pdos[str(i)][str(p[i][x]-1)]['s'])+ppdos[str(i)]['s']
        ppdos[str(i)]['p']=np.array(pdos[str(i)][str(p[i][x]-1)]['p'])+ppdos[str(i)]['p']
        ppdos[str(i)]['d']=np.array(pdos[str(i)][str(p[i][x]-1)]['d'])+ppdos[str(i)]['d']

#选中全部原子的各带中心   
for i in ppdos.keys():
    for n in obitcentre:
        x=np.array(tdosx)
        y=np.array(ppdos[i][n])
        for q in range(0,len(x)):
            if x[q] > 0:
                fer=q
                break
        x0=x[0:int(fer)]
        y0=y[0:int(fer)]
        inte_a0=np.trapz(y0,x0)
        xy=x*y
        inte_a=np.trapz(y,x)
        inte_b=np.trapz(xy,x)
        if float(inte_a) < 0.0001:
            onecenter="Null"
            tocenter="Null"
        else:
            onecenter=inte_b/inte_a
            z = np.linspace(float(onecenter),float(onecenter),nedos)
            zy= x-z
            zy2= y*zy*zy
            int_c= np.trapz(zy2,x)
            tocenter=int_c/inte_a
            onecenter=round(onecenter,3)
            tocenter=round(tocenter,3)
        print(str(i)+"\t"+str(n)+" fill is\t"+ str(round(inte_a0,3))+"\tOne center\t"+str(onecenter)+"\tTwo center\t"+str(tocenter))

import matplotlib.pyplot as plt
plt.switch_backend('agg')

X,Y1,Y2,Y3,Y4= [],[],[],[],[]
fig = plt.figure()
ax = plt.subplot(111)
X=tdosx
Y1=tdosy
plt.plot(X,Y1,linestyle='solid',label='TDOS')

for i in range(0,len(elements)):
    Y2=list(tpdos[elements[i]]['s'])
    Y3=list(tpdos[elements[i]]['p'])
    Y4=list(tpdos[elements[i]]['d'])
    plt.plot(X,Y2,linestyle='dashed',label=str(elements[i])+' s')
    plt.plot(X,Y3,linestyle='dashed',label=str(elements[i])+' p')
    plt.plot(X,Y4,linestyle='dashed',label=str(elements[i])+' d')
ax.legend(loc='upper left',prop={'size':18})
ax.spines['left'].set_linewidth(4)
ax.spines['bottom'].set_linewidth(4)
ax.spines['right'].set_linewidth(4)
ax.spines['top'].set_linewidth(4)
#ax.set_xlabel('temp',fontsize=24,labelpad = 10)
plt.xlabel("Energy/eV",fontsize=24)
plt.ylabel("DOS",fontsize=24)
ax.fill_betweenx(Y1,X , 0, facecolor="gray", color="gray",alpha=0.5)
plt.tick_params(labelsize=18)
#plt.xlim(-15,10)
#plt.ylim(0,50)
ymin,ymax=plt.ylim()
xmin,xmax=plt.xlim()
#plt.plot(0,ymax,linestyle='dashed')
#plt.xlim(-10,5)
plt.ylim(0,ymax)
plt.vlines(0, [0], ymax, color="gray", linewidth=3, linestyles="dashed")
fig.set_size_inches(18.5, 10.5)
fig.savefig('DOS.png', dpi=300)


