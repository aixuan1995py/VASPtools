#!/bin/bash

a=$1;b=$2;c=$3;
sed -i '4d' KPOINTS;
sed -i '3a '"$a"' '"$b"' '"$c"'' KPOINTS;
sed -n '4p' KPOINTS;
