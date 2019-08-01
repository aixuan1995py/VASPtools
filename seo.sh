#!/bin/bash
cd zze
bash /home/aixuan/script/pee.sh 3 > ../zzeout
for i in *;do echo $i;done > ../ii
cd ..
cd e
bash /home/aixuan/script/pee.sh 3 > ../eout
cd ..
cd $1
bash /home/aixuan/script/ee.sh 3 > ../bulk
cd ..
cd e
for i in *;do cd $i;python3 /home/aixuan/script/area.py;cd ..;done > ../area
cd ..
echo $2 > ./number
paste ii zzeout eout area bulk  number > out 
python3 /home/aixuan/script/surface.py > sur
paste ii sur > surout
rm zzeout eout bulk area number ii sur
echo "Surface energy is get!"


