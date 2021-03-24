"""Syntax: generateinstance.py FILE_NAME [NB_INSTANCES] [FINAL_RESOLUTION] [MAP_COMPLEXITY]
--> FILE_NAME is the name of the file (without the extension) where to save the instance
--> FINAL_RESOLUTION should range in [1-10], 1 being the lowest resolution (4*4),
            10 being the highest (2048*2048) resolution, the optimal is [3-5]
--> MAP_COMPLEXITY should range in [1-100], the optimal is [1-3]
--> The final picture will have NB_PATTERNS * NB_PATTERNS Perlin noise patterns
--> If MAP_COMPLEXITY is low, the picture will look like zoomed in
--> If MAP_COMPLEXITY is high, the picture will look like zoomed out
--> Default values: NB_INSTANCES = 1, FINAL_RESOLUTION = 3, MAP_COMPLEXITY = 1
"""
# $Id: 2dtexture.py 21 2008-05-21 07:52:29Z casey.duncan $
#! /usr/local/bin/python3.7

import random
import sys
from gridgen import random_noise_grid, compress_grid
from coloredmaptype import to_elevation_for_population_seed, to_elevation_for_population_iterate, to_basic_type, to_refined_type, merge_elevation_with_population, antenna_deployment_candidates
from gridtofile import grid_to_grayscale_pic_file, grid_to_elevation_map_pic_file
from population import seed_population, point_on_map, add_one_guy, point_for_adding_new_guy, point_on_map_mask, init_points_with_at_least_a_valid_neighbor, update_points_with_at_least_a_valid_neighbor
from maptoTF import get_list_agents, get_list_skills, get_agents_to_skills, remove_agents_with_no_skill_from_list_agents, remove_agents_with_no_skill_from_agents_to_skills
from TFtofile import TFtofile, TFtomapagentidstopointsrange

# ARGUMENTS THAT SHOULD BE SET
# FINAL_RESOLUTION should range from 1 to 10
# we will a target picture of resolution nb_pixels * nb_pixels,
# where nb_pixels = 2^{FINAL_RESOLUTION + 1}, so nb_pixels ranges from 4 to 2048
# for example, if FINAL_RESOLUTION = 7 then resolution of the target picture
# will be 256 * 256
FINAL_RESOLUTION = 3

# NB_PATTERNS is the number of "Perlin box patterns" per line and
# per column (optimal value is 4)
# NB_PATTERNS should range from 2 to 16
MAP_COMPLEXITY = 1

# NB_INSTANCES is the number of desired instances to be generated
NB_INSTANCES = 1

# ARGUMENTS THAT CAN BE FIXED
# POPULATION_SEED is the number of "starting cities" in the map
# POPULATION_SEED optimal value may be equal to FINAL_RESOLUTION
POPULATION_SEED = FINAL_RESOLUTION

if len(sys.argv) not in (2, 3, 4, 5) or '--help' in sys.argv or '-h' in sys.argv:
	print(__doc__)
	print('! Error: the number of arguments is wrong')
	raise SystemExit

if len(sys.argv) >= 5:
        if not sys.argv[4].isdigit():
                print(__doc__)
                print('! Error: MAP_COMPLEXITY should be an integer ranging in [1-100]')
                raise SystemExit
        nb_patterns = int(str(sys.argv[4]))
        if nb_patterns < 1 or nb_patterns > 100:
                print(__doc__)
                print('! Error: MAP_COMPLEXITY should be an integer ranging in [1-100]')
                raise SystemExit
else:
        nb_patterns = MAP_COMPLEXITY

if len(sys.argv) >= 4:
        if not sys.argv[3].isdigit():
                print(__doc__)
                print('! Error: FINAL_RESOLUTION should be an integer ranging in [1-10], 1 = lowest resolution (4*4), 10 = highest (2048*2048) resolution')
                raise SystemExit
        final_resolution = int(sys.argv[3])
        if final_resolution < 1 or final_resolution > 10:
                print(__doc__)
                print('! Error: FINAL_RESOLUTION should be an integer ranging in [1-10], 1 = lowest resolution (4*4), 10 = highest (2048*2048) resolution')
                raise SystemExit
        target_nb_pixels = 2 ** (final_resolution + 1)
else:
        final_resolution = FINAL_RESOLUTION
        target_nb_pixels = 2 ** (FINAL_RESOLUTION + 1)

if len(sys.argv) >= 3:
        if not sys.argv[2].isdigit():
                print(__doc__)
                print('! Error: NB_INSTANCES should be an integer ranging in [1-1000]')
                raise SystemExit
        nb_instances = int(sys.argv[2])
        if nb_instances < 1 or nb_instances > 1000:
                print(__doc__)
                print('! Error: NB_INSTANCES should be an integer ranging in [1-1000]')
                raise SystemExit
else:
        nb_instances = NB_INSTANCES

##population_seed = final_resolution
##total_population = 2 ** (final_resolution + 1)
##max_pop_per_box = 3
##print('population seed: ', population_seed, ', total population: ', total_population, ', max: ', max_pop_per_box)

file_name = str(sys.argv[1])

population_seed = 2 * final_resolution
total_population = 16 * (6 ** (final_resolution - 1))
max_pop_per_box = 10 * final_resolution
if final_resolution >= 5:
        neighborhood_range = 5 + (2 * (final_resolution - 4))
else:
        neighborhood_range = final_resolution
##neighborhood_range = min(final_resolution, 5)
max_type_antenna = final_resolution + 1

for id_instance in range(nb_instances):
        print('generation instance #', id_instance + 1)

        file_name_without_extension = file_name + '-' + str(id_instance + 1)

        # computing the first grid with Perlin noise
        source_grid = random_noise_grid(nb_patterns)

        # computing the target compressed grid
        target_grid = compress_grid(source_grid, target_nb_pixels)

        # format the grid to a grayscale picture and put the picture in a file
        # grid_to_grayscale_pic_file(target_grid, file_name_without_extension)

        # format the grid to a simple colored picture and put the picture in a file
        # colored_grid = to_basic_type(target_grid)
        # grid_to_elevation_map_pic_file(colored_grid, str(file_name_without_extension + "-colored"))

        # format the grid to a refined colored picture and put the picture in a file
        colored_grid = to_refined_type(target_grid)
        #grid_to_elevation_map_pic_file(colored_grid, str(file_name_without_extension + "-colored"))

        # put population
        # initialisation
        elevation_prob_grid_seed = to_elevation_for_population_seed(colored_grid)
        elevation_prob_grid_iterate = to_elevation_for_population_iterate(colored_grid)

        ##print('population seed: ', population_seed, ', total population: ', total_population, ', max: ', max_pop_per_box, ', neighborhood: ', neighborhood_range)
        population_grid = seed_population(elevation_prob_grid_seed, population_seed)
        #grid_to_elevation_map_pic_file(merge_elevation_with_population(colored_grid, population_grid, max_pop_per_box), str(file_name_without_extension + "-colored-init-populated"))

        # iterate nb_times = total desired population:
        mask_grid = init_points_with_at_least_a_valid_neighbor(population_grid, elevation_prob_grid_iterate, max_pop_per_box, neighborhood_range)
        ##counter1 = 0
        ##counter2 = 0
        print('  populate the map...')
        #print(f'  total population = {total_population}')
        for i in range(total_population):
                #if i%1000 == 0:
                #        print(f'  put guy #{i}')
        ##        if counter1 > (total_population // 10):
        ##                counter1 = 0
        ##                counter2 += 10
        ##                print('generation map: ', counter2, '%')
        ##        if i % 100 == 0:
        ##                print('population count: ', i)
        ##        if (i % 1000 == 0):
        ##                grid_to_elevation_map_pic_file(merge_elevation_with_population(colored_grid, population_grid, max_pop_per_box), str(file_name_without_extension + "-colored-" + str(i) +"-populated"))
                # 1) select a random point P1 according to the distribution given in population_grid
                random_point1 = point_on_map_mask(population_grid, mask_grid)
                # random_point1 = point_on_map(population_grid)
                # 2) select another point P2 around P1 according to the distribution given by
                # both population_grid and elevation_prob_grid
                random_point2 = point_for_adding_new_guy(population_grid, elevation_prob_grid_iterate, random_point1, max_pop_per_box, neighborhood_range)
                # 3) add a guy to that point
                if random_point2 != -1:
                        add_one_guy(population_grid, random_point2)
                if population_grid[random_point2[0]][random_point2[1]] >= max_pop_per_box:
                        # print('updating point ', random_point2, '...')
                        update_points_with_at_least_a_valid_neighbor(mask_grid, random_point2, population_grid, elevation_prob_grid_iterate, max_pop_per_box, neighborhood_range)
        ##        counter1 += 1

        ##print('generation map: done!')
        #print('  generate picture...')
        grid_to_elevation_map_pic_file(merge_elevation_with_population(colored_grid, population_grid, max_pop_per_box), str(file_name_without_extension))

        print('  generation TF instance...')
        agent_grid = antenna_deployment_candidates(colored_grid)
        ##agent_spaced = max(1, final_resolution - 2)
        ##agent_less_type = agent_spaced

        #print('    --> list agents')
        list_agents = get_list_agents(agent_grid, max_type_antenna, final_resolution)
        ##list_agents = get_list_agents(agent_grid, max_type_antenna, agent_spaced, agent_less_type)
        #print('    --> list skills')
        list_skills = get_list_skills(population_grid)
        #print('    --> agents to skills')
        agents_to_skills = get_agents_to_skills(agent_grid, population_grid, max_type_antenna, list_agents, list_skills)
        ##print('nb of agents (before): ', len(agents_to_skills))
        ##print('nb of skills: ', len(list_skills))
        #print('    --> filtering #1')
        list_agents = remove_agents_with_no_skill_from_list_agents(list_agents, agents_to_skills)
        #print('    --> filtering #2')
        agents_to_skills = remove_agents_with_no_skill_from_agents_to_skills(agents_to_skills)
        ##print('nb of agents (after): ', len(list_agents))
        ##print('list agents:')
        ##print(list_agents)
        ##print()
        ##print('nb of skills: ', len(list_skills))
        ##print('list skills:')
        ##print(list_skills)
        ##print()
        ##print('nb of agents (verif): ', len(agents_to_skills))
        ##print('agents to skills:')
        ##print(agents_to_skills)
        #print('  generate TF instance...')
        TFtofile(file_name_without_extension, list_agents, list_skills, agents_to_skills, len(colored_grid))

        # the following function call should appear if one wants to retreive the solution later on the map
        # TFtomapagentidstopointsrange(file_name_without_extension, list_agents, len(colored_grid))
