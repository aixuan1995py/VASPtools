#!/bin/bash
for i in `file * | awk '{print $2}'`
do 
if [ "$i" == "directory" ] 
then
echo "There is a directory!It will exit!"
exit
fi
done
echo "There is not a directory!It will continue!"
for i in *
do 
if [ "$i" == "INCAR" ] 
then
echo $i
elif [ "$i" == "KPOINTS" ]
then 
echo $i
elif [ "$i" == "POTCAR" ]
then 
echo $i
elif [ "$i" == "POSCAR" ]
then 
echo $i
else
rm $i
fi
done
