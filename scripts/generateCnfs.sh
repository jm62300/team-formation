#/bin/bash

# $1, the input follwowing the TF format.
# $2, the repository where are stored the files.

echo "Input team formation problem: $1"
echo "Repository where are stored the CNF output: $2"

mkdir -p $2

PATH_ENCODE="../encoder/"
sumWeight=$(grep "^a" $1 | awk '{sum+=$3 ;} END{print sum}')

name=$(basename $1 .txt)

for p in 0.01 0.03 0.05
do
    upperBound=$(echo "$sumWeight * $p" | bc | perl -nl -MPOSIX -e 'print ceil($_);')
    echo "tf generation for $upperBound as upper bound"
    $PATH_ENCODE/encode.py $1 -tf -b=$upperBound > $2/tf_${name}_${p}_${upperBound}.cnf

    for k in 2 3 4
    do
        echo "ktf generation for $upperBound as upper bound and k=$k"
        $PATH_ENCODE/encode.py $1 -ktf -k=$k -b=$upperBound > $2/ktf_${name}_${k}_${p}_${upperBound}.cnf
    done
done

