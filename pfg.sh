#!/bin/bash
a=$1;b=$2;c=$3

if [ "$c" == "ee" ];then 
    for ((n=$a;n>=$b;n--));do 
        cd $n;
        echo $n;
        for i in *;do 
            cd $i;
            if [ -f OUTCAR ];then
                E=`grep '  without' OUTCAR |tail -n 1 |awk '{print $7}'`;
            elif [ -f OUTCAR.gz ];then
                E=`zgrep '  without' OUTCAR.gz --binary-files=text  |tail -n 1 |awk '{print $7}'`;
            else
                echo "Puck!"
            fi;
            cd ..;
            echo -e $i"\t"$E;
        done;
        cd ..;
    done;
elif [ "$c" == "zpe" ];then
    for ((n=$a;n>=$b;n--));do 
        cd $n;
        echo $n;
        for i in *;do
            cd $i;
            if [ -f OUTCAR ];then
                ZPE=`grep 'f  =' OUTCAR | awk '{print $10}' | paste -sd+ |bc`;
            elif [ -f OUTCAR.gz ];then
                ZPE=`zgrep 'f  =' OUTCAR.gz --binary-files=text  | awk '{print $10}' | paste -sd+ |bc`;
            else
                echo "Puck!"
            fi;            
            cd ..;
            echo -e $i"\t"$ZPE;
        done;
    cd ..;
    done;
else
    echo "Fuck!"
fi;
