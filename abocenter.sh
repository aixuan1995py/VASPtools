#!/bin/bash

a=$1;
mkdir DOS;
mkdir DOS/$a;
for n in {1..10};
do sed '1d' DOS$a | awk -v t=$n '{print $t}' >> DOS/$a/$n;
done;
cd DOS;

cd $a;
x=` grep -c - 1 `;y=$(($x+1));
for n in {1..10};do sed -i ''"$y"',$d' $n;done;
cd ..;

cd $a;
a=`python3 /home/aixuan/script/dos/1dcenter.py | grep intea | awk '{print $3}' `;
b=`python3 /home/aixuan/script/dos/1dcenter.py | grep inteb | awk '{print $3}' `;
cd ..;echo -e $a"\t"$b >> out;
a=`cat out | awk '{print $1}' | paste -sd+ |bc`;
b=`cat out | awk '{print $2}' | paste -sd+ |bc`;
n=`expr $b/$a`;
cen=`echo -e $a"\t"$b | awk '{print $2/$1}'`;
echo -e $a"\t"$b"\t"$cen
cd ..;
rm -r DOS;