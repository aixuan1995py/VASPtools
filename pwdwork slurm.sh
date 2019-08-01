#!/bin/bash
pwd_work=$(scontrol show job $1 | grep WorkDir | awk -F [=] '{print $2 }')
echo $pwd_work
cd $pwd_work
