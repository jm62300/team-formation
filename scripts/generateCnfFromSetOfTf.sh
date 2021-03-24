#!/bin/bash

# $1, the repository containing the TF problems.
# $2, the repository where will be stored the CNF formula.

mkdir -p $2
name=$(basename $1)

for f in $(find $1 -name "*.t*")
do
    ./generateCnfs.sh $f $2/$name
done
