#!/bin/bash
a=$1

if [ "$a" == "1" ];
then 
grep ' energy   TOTEN' OUTCAR | awk '{print $5}'
elif [ "$a" == "2" ]; 
then
grep '  without' OUTCAR |tail -n 1 |awk '{print $4}'
elif [ "$a" == "3" ]; 
then
grep '  without' OUTCAR |tail -n 1 |awk '{print $7}'
else
echo "Fuck!"
fi;
