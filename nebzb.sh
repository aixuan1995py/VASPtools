#!/bin/bash

a=`dist.pl ini/CONTCAR fin/CONTCAR`
echo $a
echo "Please Input Your Number!"
read num
nebmake.pl ini/CONTCAR fin/CONTCAR $num
nebmovie.pl
cp ini/OUTCAR 00/
b=`ls -d */ |tail -3 | sed -n '1p'`
cp fin/OUTCAR $b