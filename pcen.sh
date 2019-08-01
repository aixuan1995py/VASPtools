#!/bin/bash
a=$1;b=$2;
echo $a;echo $b;
for n in *;
do cd $n;
dd=`perl /home/aixuan/script/vtstscripts-935/dosanalyze.pl e=-50,50 d $a-$b | grep Aver | awk '{print $5}' `;
cd ..;
echo -e $n"\t"$dd;
done
