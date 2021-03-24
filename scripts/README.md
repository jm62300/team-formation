# TF to CNF scripts

This repository contains two bash scripts:
* generateCnfs.sh, takes as input a TF instance a generate several CNF formula
in a given output repository (we consider tf and ktf (k in {2,3,4}))
for several bounds compute as a pourcentage of the sum of the agents' weight
(pourcentage in {10,20,30,40,50}));
```bash
./generateCnfs.sh ../examples/aamas/0-simple-examples/simple-example2.txt cnfs
```
* generateCnfFromSetOfTf.sh, take as parameter a repository that contains
tf formula (with .txt as extension) and calls the previous script on all
the problems and store the CNF formula in the given repository;
```bash
./generateCnfs.sh ../examples/aamas/0-simple-examples/ cnfs
```
*generateMain.sh is used to realize multiple call of generatecnffromsetoftf.sh
on several repository.