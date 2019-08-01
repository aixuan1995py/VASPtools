# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 2018

@author: Vacian
"""

import numpy
import string
import argparse
from scipy import integrate
#Read d State Files
#1 is x axis;2 is s obits;3-5 is p obits;6-10 is d obits
x = numpy.loadtxt('1')
a = numpy.loadtxt('6')
b = numpy.loadtxt('7')
c = numpy.loadtxt('8')
d = numpy.loadtxt('9')
e = numpy.loadtxt('10')
#Plus all d Files
y =a+b+c+d+e
#Formulas b
xy=x*y
#Integrate
inte_a= numpy.trapz(y,x)
inte_b= numpy.trapz(xy,x)
onecenter=inte_b/inte_a
#Out
print("One Moment Center is 'b/a'")
print("intea is "+ str(inte_a))
print("inteb is "+ str(inte_b))
print("One Moment Center is "+str(onecenter))
#Get Centerplus From Shell
parser = argparse.ArgumentParser()
parser.add_argument("intc", help="Get Center！",type=float)
arg = parser.parse_args()
center=float(arg.intc)
print (center)
#Get Centerplus Array
z = numpy.linspace(center,center,len(a))
#Formulas c
zy= x-z
zy2= y*zy*zy
int_c= numpy.trapz(zy2,x)
#Out
print("Two Moment Center is 'c/a c=b*(x-center)^2'")
print("Inc is "+ str(int_c))
tocenter=int_c/inte_a
print("Two Moment Center is "+str(tocenter))