#!/bin/bash
a=$1;b=$2;c=$3

if [ "$c" == "ee" ];
then 
for ((n=$a;n>=$b;n--));
do cd $n;echo $n;for i in *;do cd $i;
E=`grep '  without' OUTCAR |tail -n 1 |awk '{print $7}'`;
cd ..;echo -e $i"\t"$E;
done;
cd ..;
done;
elif [ "$c" == "zpe" ]; 
then
for ((n=$a;n>=$b;n--));
do cd $n;echo $n;
for i in *;
do cd $i;
ZPE=`grep 'f  =' OUTCAR | awk '{print $10}' | paste -sd+ |bc`;
cd ..;
echo -e $i"\t"$ZPE;
done;
cd ..;
done;
else
echo "Fuck!"
fi;
