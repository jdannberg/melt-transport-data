#!/bin/bash

gawk 'BEGIN{FS = "[ =]+"}; /Errors/ {print $7, $8, $9, $10}' $1 | tail -1 > $1.last-step.csv
