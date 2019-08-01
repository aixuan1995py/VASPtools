#!/bin/bash

a=$1;b=$2;aa=$a;bb=$b
mkdir DOS;
for ((v=$a;v<=$b;v++));
do mkdir DOS/$v;
for n in {1..10};
do sed '1d' DOS$v | awk -v t=$n '{print $t}' >> DOS/$v/$n;
done;
done;
cd DOS;
for ((v=$aa;v<=$bb;v++));
do cd $v;
a=`python3 /home/aixuan/script/dos/1dcenter.py | grep intea | awk '{print $3}' `;
b=`python3 /home/aixuan/script/dos/1dcenter.py | grep inteb | awk '{print $3}' `;
cd ..;echo -e $a"\t"$b >> out;done;
a=`cat out | awk '{print $1}' | paste -sd+ |bc`;
b=`cat out | awk '{print $2}' | paste -sd+ |bc`;
n=`expr $b/$a`;
cen=`echo -e $a"\t"$b | awk '{print $2/$1}'`;
echo "One Moment Center is";echo $cen;
for ((v=$aa;v<=$bb;v++));
do cd $v;
a=`python3 /home/aixuan/script/dos/12dcenter.py $cen | grep intea | awk '{print $3}' `;
b=`python3 /home/aixuan/script/dos/12dcenter.py $cen | grep Inc | awk '{print $3}' `;
cd ..;
echo -e $a"\t"$b >> out2;
done;
a=`cat out2 | awk '{print $1}' | paste -sd+ |bc`;
b=`cat out2 | awk '{print $2}' | paste -sd+ |bc`;
n=`expr $b/$a`;cen=`echo -e $a"\t"$b | awk '{print $2/$1}'`;
echo "Two Moment Center is";echo $cen