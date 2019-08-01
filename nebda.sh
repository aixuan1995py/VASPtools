#!/bin/bash
#Neb data copy and do something

a=$1;
filepath="./out$a"
if [ -d $filepath ];
then
rm -r out$a
echo "Outfiles is exit! I will remove it and then do next!"
cp -r $a out$a
cd out$a
nebresults.pl
else
cp -r $a out$a
cd out$a
nebresults.pl
fi