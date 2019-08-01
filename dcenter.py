# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 18:30:05 2018

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

downin= numpy.trapz(y,x)
upin= numpy.trapz(xy,x)
center=upin/downin
print("upin is "+ str(upin))
print("downin is "+ str(downin))
print("Center is "+str(center))
