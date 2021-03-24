#!/usr/bin/python3
# Copyright (C) 2021  Lagniez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from agent import *
from parser import *

from tf import *
from ktf import *

import sys
import os

def help():
    print("USAGE: ./solve.py FILE [-tf] [-ktf] [-k=1] [-b=1]")
    exit(1)

if len(sys.argv) <= 1 or sys.argv[1] in ["-h", "-help"]:
    help()

fileName = str(sys.argv[1])
k, m, b = 1, "tf", 1

# parse the options
for o in sys.argv[2:]:
    if o in ["-tf", "-ktf"]:
        m = o[1:]
    if o[:3] == "-k=":
        k = int(o.split('=')[1])
    if o[:3] == "-b=":
        b = int(o.split('=')[1])

print("c Options:")
print("c Method we run:", m)
print("c The number of agents we can loose:", k)
print("c The bound:", b)

print("c input file:", fileName)
nbAgents, nbSkills, mapOfAgents, mapOfSkills, eclauses = parse(fileName)

print("c Information about the problem: ")
print("c Number of agents:", nbAgents)
print("c Number of skills:", nbSkills)
print("c Number of integrity constraints:", len(eclauses))

# apply the translation
agentsProp, skillsProp = [], []
if(m == "tf"):
    solveTF(nbAgents, nbSkills, mapOfAgents, mapOfSkills, eclauses, b)
elif(m == "ktf"):
    solvekTF(nbAgents, nbSkills, mapOfAgents, mapOfSkills, eclauses, k)
