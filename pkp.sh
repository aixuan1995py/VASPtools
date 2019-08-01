#!/bin/bash

a=$1;b=$2;c=$3;
for i in *;do cd $i;echo $i;bash /home/aixuan/script/kp.sh $a $b $c;cd ..;done
