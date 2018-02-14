#!/bin/bash

i=1
for f in *.JPG ;
do
    mv $f $i.JPG
    python resize.py
    rm -rf $i.JPG
    i=$((i+1))
    echo $i
done
