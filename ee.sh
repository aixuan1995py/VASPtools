#!/bin/bash
a=$1

if [ -f OUTCAR ];then
    if [ "$a" == "1" ];then
        grep ' energy   TOTEN' OUTCAR | awk '{print $5}'
    elif [ "$a" == "2" ];then
        grep '  without' OUTCAR |tail -n 1 |awk '{print $4}'
    elif [ "$a" == "3" ];then
        grep '  without' OUTCAR |tail -n 1 |awk '{print $7}'
    elif [ "$a" == "4" ];then
        grep 'f  =' OUTCAR | awk '{print $10}' | paste -sd+ |bc
    else
        echo "Puck!"
    fi;
elif [ -f OUTCAR.gz ];then
    if [ "$a" == "1" ];then 
        zgrep ' energy   TOTEN' OUTCAR.gz --binary-files=text  | awk '{print $5}'
    elif [ "$a" == "2" ];then
        zgrep '  without' OUTCAR.gz --binary-files=text  |tail -n 1 |awk '{print $4}'
    elif [ "$a" == "3" ];then
        zgrep '  without' OUTCAR.gz --binary-files=text  |tail -n 1 |awk '{print $7}'
    elif [ "$a" == "4" ];then
        zgrep 'f  =' OUTCAR.gz --binary-files=text  | awk '{print $10}' | paste -sd+ |bc
    else
        echo "Puck!"
    fi;
else
    echo "Puck!"
fi;