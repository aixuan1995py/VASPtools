#!/bin/bash
a=$1;b=$2;
cat DOS0 | awk '{print $1}' > x;
mkdir DOS;
for ((v=$a;v<=$b;v++));
do mkdir DOS/$v;
    for n in {1..10};
    do sed '1d' DOS$v | awk -v t=$n '{print $t}' >> DOS/$v/$n;
    done;
    cd DOS;
    cd $v;
    paste 2 >> s;
    paste 3 4 5 >> p;
    paste 6 7 8 9 10 >> d;
    cat d |awk '{printf "%12.8f\n",$1+$2+$3+$4+$5}' >> dp;
    cat s |awk '{printf "%12.8f\n",$1}' >> sp;
    cat p |awk '{printf "%12.8f\n",$1+$2+$3}' >> pp;
    cd ..;
    cd ..;
done;
cd DOS;
mkdir -p spp/spp;
mkdir -p dpp/dpp;
mkdir -p ppp/ppp;
for b in *;
do 
if [ "$b" == "spp" ];
then 
echo s;
elif [ "$b" == "dpp" ];
then echo p;
elif [ "$b" == "ppp" ];
then echo d;
else
    cp $b/sp spp/spp/sp$b;
    cp $b/dp dpp/dpp/dp$b;
    cp $b/pp ppp/ppp/pp$b;
fi;
done;

for q in {spp,ppp,dpp};
do cd $q;
    cd $q;
    touch ../111;
    for i in *;
    do  paste $i ../111 > ../222;
        cat ../222 | awk '{printf "%12.8f\n",$1+$2}' > ../333;
        rm ../111;
        rm ../222;
        mv ../333 ../111;
    done;
    cd ..;
    cd ..;
done;
cd ..;

paste x DOS/spp/111 > s;
paste x DOS/dpp/111 > d;
paste x DOS/ppp/111 > p;
paste DOS/spp/111 DOS/dpp/111 DOS/ppp/111 > spd;
cat spd | awk '{printf "%12.8f\n",$1+$2+$3}' >> a;
paste x a spd > all;

python3 /home/aixuan/script/dos/dosplot.py
