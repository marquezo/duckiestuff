#!/bin/bash
while IFS='' read -r line; do
    cp $line project/train_data/$2/
done < "$1"
