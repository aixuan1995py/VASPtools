#!/bin/bash
mkdir $1
echo -e "You have mkdir $1"

for i in *
do
cd $i
mkdir $2
for n in *
do 
cd $n
cp /home/aixuan/script/tras/* ./
cd ..
echo -e "You have mkdir $i $n,and copy"
done
cd ..
done

