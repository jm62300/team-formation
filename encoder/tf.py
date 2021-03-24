#!/usr/bin/python3

from docplex.mp.model import Model
from agent import *


def solveTF(nbAgents, nbSkills, mapOfAgents, mapOfSkills, eclauses):
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
    """
    model = Model()
    agentsProp = [model.binary_var(str(i)) for i in range(nbAgents)]

    # the set of constraints that ensure that each skill is supported by at least one agent
    for s in mapOfSkills:
        model.add_constraint(model.sum(agentsProp[mapOfAgents[a].id] for a in mapOfSkills[s].l) >= 1)

    # integrity constraints
    for cl in eclauses:
        model.add_constraint(model.sum(agentsProp[mapOfAgents[cl[i]].id] for i in range(len(cl))) <= 1)

    # the function we search to minimize
    cost = model.sum(agentsProp[mapOfAgents[a].id] * mapOfAgents[a].w1 for a in mapOfAgents)

    model.minimize(cost)
    solution = model.solve()

    if solution != None:
        print("v", end=" ")
        for a in agentsProp:
            if(solution[a] == 1):
                print(a, end=" ")
        print()
        print("o", int(model.objective_value))
    else:
        print("No folution found")


def toTF(nbAgents, nbSkills, mapOfAgents, mapOfSkills, eclauses, outputFile):
    # create boolean variable indexes
    agentsProp = [i for i in range(1, nbAgents + 1)]
    idxFresh = agentsProp[-1] + 1

    print("c map for agents (in the order): ", str(agentsProp))

    # constraint we want to optimize
    print("min: ", end="", file=outputFile)
    for a in mapOfAgents:
        agent = mapOfAgents[a]
        print("+" + str(agent.w1) + "*x" + str(agentsProp[agent.id]), end=" ", file=outputFile)
    print(";", file=outputFile)

    for s in mapOfSkills:
        for a in mapOfSkills[s].l:
            print("+1*x" + str(agentsProp[mapOfAgents[a].id]), end=" ", file=outputFile)
        print(" >=", 1, ";", file=outputFile)

    # integrity constraints
    for cl in eclauses:
        for i in range(len(cl)):
            assert cl[i] in mapOfAgents
            print("+1*x" + str(agentsProp[mapOfAgents[cl[i]].id]), end=" ", file=outputFile)
        print(" <= 1 ;", file=outputFile)

    outputFile.flush()
    return agentsProp
