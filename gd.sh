#!/bin/bash

a=$1;
b=$(($a+9));
sed -i "10,"$b"s/T/F/g" POSCAR;
