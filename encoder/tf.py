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
from pysat.pb import *

def solveTF(nbAgents, nbSkills, mapOfAgents, mapOfSkills, eclauses, bound):
    """
    Solve the TF problem given the input variables.

    Attributes:
    ----------
    nbAgents : int
        the number of agents
    nbSkills : int
        the number of skills
    mapOfAgents : map
        for each id of agent we associate a structure that store data about it
    mapOfSkills : map
        for each id of skill we associate a structure that store data about it
    eclause : list
        each element containt an exclusion list
    bound : int
        the maximum value for the objective function
    """
    agentsProp = [i + 1 for i in range(nbAgents)]
    clauses = []

    # the set of constraints that ensure that each skill is supported by at least one agent
    for s in mapOfSkills:
        clauses.append([agentsProp[mapOfAgents[a].id] for a in mapOfSkills[s].l])

    # integrity constraints
    for cl in eclauses:
        for i in range(len(cl)):
            for j in range(i+1, len(cl)):
                clauses.append([-agentsProp[mapOfAgents[cl[i]].id], -agentsProp[mapOfAgents[cl[j]].id]])

    # the function we search to minimize
    agents = [agentsProp[mapOfAgents[a].id] for a in mapOfAgents]
    weights = [mapOfAgents[a].w1 for a in mapOfAgents]

    print(agents)
    print(weights)

    cnf = PBEnc.leq(lits=agents, weights=weights, bound=bound, encoding=EncType.bdd)
    clauses += cnf.clauses

    # print out following the Dimacs format.
    print("p cnf", nbAgents, len(clauses))
    for cl in clauses:
        for l in cl:
            print(l, end=" ")
        print("0")
