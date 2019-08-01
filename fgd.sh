#!/bin/bash
for i in `ls | sort -r`
do cd $i
echo -e "Now is in $i"
for n in *
do cd $n
echo -e "Now is in $i $n"
a=0
for s in `sed -n '7p' POSCAR`
do a=$(($a+$s))
done
f=$(($a+10))
echo -e "$f to end line is delete!"
sed -i ''$f',$d' POSCAR
sed -i "$((1+$i))d" /home/aixuan/script/poscar/$n
sed -i "s/\r//" POSCAR
sed -i "6s/$/ H/g" POSCAR
sed -i "7s/$/ $(($i))/g" POSCAR
cat /home/aixuan/script/poscar/$n>> POSCAR
echo -e "$i adso.  is add to $n!"
cd ..
done
cd ..
done
