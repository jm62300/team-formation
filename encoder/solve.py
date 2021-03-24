#!/usr/bin/python3
from agent import *
from parser import *

from tf import *
from ktf import *
from ptf import *
from rtf import *

import sys
import os
import time
from math import ceil

start_time = time.time()

def help():
    print("USAGE: ./solve.py FILE [-tf] [-ktf] [-ptf] [-rtf] [-k=1] [-t=90] [-cut] [-path=PATH]")
    exit(1)

if len(sys.argv) <= 1 or sys.argv[1] in ["-h", "-help"]:
    help()

fileName = str(sys.argv[1])
k, t, m, cut = 1, 90, "tf", False

# parse the options
for o in sys.argv[2:]:
    if o in ["-tf", "-ktf", "-ptf", "-rtf"]:
        m = o[1:]
    if o[:3] == "-k=":
        k = int(o.split('=')[1])
    if o[:3] == "-t=":
        t = int(o.split('=')[1])
    if o == "-cut":
        cut = True
    if o[:6] == "-path=":
        path = o.split('=')[1]

print("c Options:")
print("c Method we run:", m)
print("c The number of agents we can loose:", k)
if (m == "ptf" or m == "rtf"):
    print("c Cut used:", cut)
if (m == "ptf"):
    print("c Threshold concerning the quantity of skills we can lost:", t)

print("c input file:", fileName)
nbAgents, nbSkills, mapOfAgents, mapOfSkills, eclauses = parse(fileName)

print("c Information about the problem: ")
print("c Number of agents:", nbAgents)
print("c Number of skills:", nbSkills)
print("c Number of clauses:", len(eclauses))

# apply the translation
agentsProp, skillsProp = [], []
if(m == "tf"):
    solveTF(nbAgents, nbSkills, mapOfAgents, mapOfSkills, eclauses)
elif(m == "ktf"):
    solvekTF(nbAgents, nbSkills, mapOfAgents, mapOfSkills, eclauses, k)

interval = time.time() - start_time
print ('t', interval)
