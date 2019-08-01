#!/bin/bash

a=$1;
b=$(($a+9));
for i in *;do sed -i "10,"$b"s/T/F/g" $i/POSCAR;done
