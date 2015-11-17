#!/bin/bash

for i in $( ls log-*.txt ); do
    gawk 'BEGIN{FS = "[ =]+"}; /Timestep/ {ORS = ", "; print $5; ORS="\n"}; /Errors/ {print $7, $8, $9, $10}' $i > $i.csv
done
