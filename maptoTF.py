from population import points_around

TYPE_1_COST1 = 1
TYPE_2_COST1 = 2
TYPE_3_COST1 = 3
TYPE_4_COST1 = 4
TYPE_5_COST1 = 5
TYPE_6_COST1 = 6
TYPE_7_COST1 = 7

TYPE_1_COST2 = 1
TYPE_2_COST2 = 2
TYPE_3_COST2 = 3
TYPE_4_COST2 = 4
TYPE_5_COST2 = 5
TYPE_6_COST2 = 6
TYPE_7_COST2 = 7

TYPE_1_RANGE = 0
TYPE_2_RANGE = 1
TYPE_3_RANGE = 2
TYPE_4_RANGE = 3
TYPE_5_RANGE = 4
TYPE_6_RANGE = 5
TYPE_7_RANGE = 6

'''
input: the antenna type id
output: a 3-vector (cost1, cost2, range) for this antenna type
'''
def get_type_agent(id_antenna, final_resolution):
    if final_resolution == 1:
        switcher = {
            1: [TYPE_1_COST1, TYPE_1_COST2, TYPE_1_RANGE],
            2: [TYPE_2_COST1, -1, TYPE_2_RANGE],
            3: [TYPE_3_COST1, -1, TYPE_3_RANGE],
            4: [TYPE_4_COST1, -1, TYPE_4_RANGE],
            5: [TYPE_5_COST1, -1, TYPE_5_RANGE],
            6: [TYPE_6_COST1, -1, TYPE_6_RANGE],
            7: [TYPE_7_COST1, -1, TYPE_7_RANGE]
        }
    elif final_resolution in (2, 3):
        switcher = {
            1: [TYPE_1_COST1, TYPE_1_COST2, TYPE_1_RANGE],
            2: [TYPE_2_COST1, TYPE_2_COST2, TYPE_2_RANGE],
            3: [TYPE_3_COST1, -1, TYPE_3_RANGE],
            4: [TYPE_4_COST1, -1, TYPE_4_RANGE],
            5: [TYPE_5_COST1, -1, TYPE_5_RANGE],
            6: [TYPE_6_COST1, -1, TYPE_6_RANGE],
            7: [TYPE_7_COST1, -1, TYPE_7_RANGE]
        }
    elif final_resolution in (4, 5):
        switcher = {
            1: [TYPE_1_COST1, TYPE_1_COST2, TYPE_1_RANGE],
            2: [TYPE_2_COST1, TYPE_2_COST2, TYPE_2_RANGE],
            3: [TYPE_3_COST1, TYPE_3_COST2, TYPE_3_RANGE],
            4: [TYPE_4_COST1, -1, TYPE_4_RANGE],
            5: [TYPE_5_COST1, -1, TYPE_5_RANGE],
            6: [TYPE_6_COST1, -1, TYPE_6_RANGE],
            7: [TYPE_7_COST1, -1, TYPE_7_RANGE]
        }
    elif final_resolution in (5, 6):
        switcher = {
            1: [TYPE_1_COST1, TYPE_1_COST2, TYPE_1_RANGE],
            2: [TYPE_2_COST1, TYPE_2_COST2, TYPE_2_RANGE],
            3: [TYPE_3_COST1, TYPE_3_COST2, TYPE_3_RANGE],
            4: [TYPE_4_COST1, TYPE_4_COST2, TYPE_4_RANGE],
            5: [TYPE_5_COST1, -1, TYPE_5_RANGE],
            6: [TYPE_6_COST1, -1, TYPE_6_RANGE],
            7: [TYPE_7_COST1, -1, TYPE_7_RANGE]
        }
    elif final_resolution in (7, 8):
        switcher = {
            1: [TYPE_1_COST1, TYPE_1_COST2, TYPE_1_RANGE],
            2: [TYPE_2_COST1, TYPE_2_COST2, TYPE_2_RANGE],
            3: [TYPE_3_COST1, TYPE_3_COST2, TYPE_3_RANGE],
            4: [TYPE_4_COST1, TYPE_4_COST2, TYPE_4_RANGE],
            5: [TYPE_5_COST1, TYPE_5_COST2, TYPE_5_RANGE],
            6: [TYPE_6_COST1, -1, TYPE_6_RANGE],
            7: [TYPE_7_COST1, -1, TYPE_7_RANGE]
        }
    else:
        switcher = {
            1: [TYPE_1_COST1, TYPE_1_COST2, TYPE_1_RANGE],
            2: [TYPE_2_COST1, TYPE_2_COST2, TYPE_2_RANGE],
            3: [TYPE_3_COST1, TYPE_3_COST2, TYPE_3_RANGE],
            4: [TYPE_4_COST1, TYPE_4_COST2, TYPE_4_RANGE],
            5: [TYPE_5_COST1, TYPE_5_COST2, TYPE_5_RANGE],
            6: [TYPE_6_COST1, TYPE_6_COST2, TYPE_6_RANGE],
            7: [TYPE_7_COST1, -1, TYPE_7_RANGE]
        }
    return switcher.get(id_antenna, [])

'''
agent_grid is a True-False grid, True iff an antenna can be deployed
nb_types: the number of antenna types we want (not more than 7)
The function returns list_agents, where each agent is a 6-vector: (point, id_point, cost1, cost2, range, id_agent)
id_point is an incremental 1-dim version of point
agent_spaced is used to space antennas to simplify the problem, it 1 by default.
--> if agent_spaced = 1, then an antenna can be deployed on every box.
--> if agent_spaced = 2, then an antenna can be deployed only every 2*2 boxes.
--> if agent_spaced = 3, then an antenna can be deployed only every 3*3 boxes.
agent_less_type is used to deploy less types of antennas on the map, it is 1 by default.
--> if agent_less_type = 1, then types 1, 2, 3, 4, 5, ... will be deployed
--> if agent_less_type = 2, then types 1, 3, 5, ... will be deployed
--> if agent_less_type = 3, then types 1, 4, 7, ... will be deployed
'''
def get_list_agents(agent_grid, nb_types, final_resolution, agent_spaced=1, agent_less_type=1):
    result = []
    grid2d_length = len(agent_grid)
    id_point = 0
    id_agent = 0
    for x in range(grid2d_length):
        for y in range(grid2d_length):
            if agent_grid[x][y] and x % agent_spaced == 0 and y % agent_spaced == 0:
                for i in range(1, nb_types + 1, agent_less_type):
                    element_agent = []
                    point = []
                    point.append(x)
                    point.append(y)
                    element_agent.append(point)
                    element_agent.append(id_point)
                    element_agent.append(get_type_agent(i,final_resolution)[0])
                    element_agent.append(get_type_agent(i,final_resolution)[1])
                    element_agent.append(get_type_agent(i,final_resolution)[2])
                    element_agent.append(id_agent)
                    result.append(element_agent)
                    id_agent += 1
                id_point += 1
    return result

'''
population_grid is the population density grid
The function returns list_skills, where each skill is a 2-vector: (point, population)
'''
def get_list_skills(population_grid):
    result = []
    grid2d_length = len(population_grid)
    for x in range(grid2d_length):
        for y in range(grid2d_length):
            if population_grid[x][y] > 0:
                element_skill = []
                point = []
                point.append(x)
                point.append(y)
                element_skill.append(point)
                element_skill.append(population_grid[x][y])
                result.append(element_skill)
    return result

def get_id_skill(point, list_skills):
    list_skills_length = len(list_skills)
    for i in range(list_skills_length):
        if list_skills[i][0][0] == point[0] and list_skills[i][0][1] == point[1]:
            return i

    return -1

'''
agent_grid is a True-False grid, True iff an antenna can be deployed
population_grid is the population density grid
nb_types: the number of antenna types we want (not more than 7)
The function returns agents_to_skills, an array associating each agent id to a list of skill ids
'''
def get_agents_to_skills(agent_grid, population_grid, nb_types, list_agents, list_skills):
    result = []
    grid2d_length = len(agent_grid)
    nb_agents = len(list_agents)
    for id_agent in range(nb_agents):
        list_skills_for_id_agent = []
        neighbor_list = points_around(list_agents[id_agent][0], list_agents[id_agent][4], grid2d_length, True)
        for neighbor in neighbor_list:
            id_skill = get_id_skill(neighbor, list_skills)
            # here, if id_skill == -1 this means that point neighbor has no population
            if id_skill >= 0:
                list_skills_for_id_agent.append(id_skill)
        result.append(list_skills_for_id_agent)
    return result

'''
Based on agents_to_skills we make a new array filtering list_agents
'''
def remove_agents_with_no_skill_from_list_agents(list_agents, agents_to_skills):
    result = []
    new_id_agent = 0
    init_nb_agents = len(agents_to_skills)
    for i in range(init_nb_agents):
        if agents_to_skills[i]:
            list_agents[i][5] = new_id_agent
            new_id_agent += 1
            result.append(list_agents[i])
    return result

'''
Return a filtered list of agents_to_skills removing agents with no skill

'''
def remove_agents_with_no_skill_from_agents_to_skills(agents_to_skills):
    result = []
    init_nb_agents = len(agents_to_skills)
    for i in range(init_nb_agents):
        if agents_to_skills[i]:
            result.append(agents_to_skills[i])
    return result

##'''
##agent_grid is a True-False grid, True iff an antenna can be deployed
##population_grid is the population density grid
##nb_types: the number of antenna types we want (not more than 7)
##The function creates:
##list_agents: each agent is a 4-vector: (point, cost1, cost2, range)
##list_skills: each skill is a 2-vector: (point, population)
##agents_to_skills: an array associating each agent id to a list of skill ids
##'''
##def map_to_TF(agent_grid, population_grid, nb_types, list_agents, list_skills, agents_to_skills):
##    list_agents = []
##    list_skills = []
##    agents_to_skills = []
##
##    # computes first the list of agents using agent_grid
##    # list_agents = get_list_agents(agent_grid, nb_types)
##
##    # computes now the list of skills using population_grid
##    # list_skills = get_list_skills(population_grid)
##
##    # computes the mapping agents_to_skills
##
##    # remove from list_agents the agents with no skill
