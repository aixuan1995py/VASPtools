# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 2018
#单个原子的计算 不完整 需要输入
@author: Vacian
"""

import numpy
from scipy import integrate

x = numpy.loadtxt('1')
a = numpy.loadtxt('6')
b = numpy.loadtxt('7')
c = numpy.loadtxt('8')
d = numpy.loadtxt('9')
e = numpy.loadtxt('10')
y =a+b+c+d+e
xy=x*y

inte_a= numpy.trapz(y,x)
inte_b= numpy.trapz(xy,x)
#center=inte_b/inte_a

print("One Moment Center is 'b/a'")
print("intea is "+ str(inte_a))
print("inteb is "+ str(inte_b))
#print("One Moment Center is "+str(center))
print("Please Enter Center")
center=input()
ncenter=float(str(center))
z = numpy.linspace(ncenter,ncenter,len(a))
zy= x-z
zy2= y*zy*zy
int_c= numpy.trapz(zy2,x)

print("Two Moment Center is 'c/a c=b*(x-center)^2'")
print("c is "+ str(int_c))
centerx=int_c/inte_a
print("Two Moment Center is "+str(centerx))