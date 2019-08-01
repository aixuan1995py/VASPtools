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
python3 /home/aixuan/script/area.py > ./area
echo $2 > ./number
paste ii zzeout eout bulk area number > out 
python3 /home/aixuan/script/surface.py > sur
paste ii sur > surout
rm zzeout eout bulk area number ii sur
echo "Surface energy is get!"


