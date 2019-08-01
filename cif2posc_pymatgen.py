# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:57:00 2019

@author: Xuan Ai
"""

import pymatgen as mg
import os

path=os.getcwd()
files=os.listdir(path)
cifs=[]
for i in files:
    if ".cif" in i:
        cifs.append(i)

        
def tra(filename):
    structure = mg.Structure.from_str(open(filename).read(), fmt="cif")
    pos_file_obj=mg.io.vasp.Poscar(structure)
    pos_file_obj.write_file(filename+'.out')
    fileline=[]
    with open (filename+'.out','r',encoding='UTF-8') as f:
            lines=f.readlines()
            for line in lines:
                fileline.append(line.strip().split())
    
    fileline[7][0]='Direct'
    
    for i in range(8,len(fileline)):
        fileline[i]=fileline[i][0:3]
    if len(cifs) != 1:
        with open(filename+'.vasp','w') as f:
            for line in fileline:
                f.write(("    ").join(line)+"\n")
    else:
        with open("POSCAR",'w') as f:
            for line in fileline:
                f.write(("    ").join(line)+"\n")
for i in cifs:
    tra(i)