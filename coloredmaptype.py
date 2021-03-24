# predefined colors for landscape
SEA = [65,105,225]
LAND = [34,139,34]
BEACH = [238, 214, 175]
##DENSELY_POPULATED = [15, 80, 15]
##MODERATELY_POPULATED = [25, 105, 25]
##LOSELY_POPULATED = [144, 238, 144]
DENSELY_POPULATED = [178, 154, 115]
MODERATELY_POPULATED = [198, 174, 135]
LOSELY_POPULATED = [218, 194, 155]
DESERT = [238, 214, 175]
MOUNTAIN = [235, 235, 235]

# for initial probability distributions (for seeds)
PROB_DENSELY = 4
PROB_MODERATELY = 2
PROB_LOSELY = 1
PROB_NO_POPULATION = 0

# for growing population probability distributions (for iterations)
PROB_DENSELY_ITERATE = 8
PROB_MODERATELY_ITERATE = 4
PROB_LOSELY_ITERATE = 2
PROB_DESERT_ITERATE = 1

# tmp population seed (black color)
SOMEONE = [0, 0, 0]

import random

'''
This function projects the source_grid into another grid where each color
is mapped to another color
'''
def to_basic_type(source_grid):
    result= []
    grid_length = len(source_grid)
    for x in range(grid_length):
        line = []
        for y in range(grid_length):
            if source_grid[x][y] < 120:
                line.append(SEA)
            elif source_grid[x][y] < 130:
                line.append(BEACH)
            else:
                line.append(LAND)
        result.append(line)
    return result

'''
This function projects the source_grid into another grid where each color
is mapped to another color
'''
def to_refined_type(source_grid):
    result= []
    grid_length = len(source_grid)
    for x in range(grid_length):
        line = []
        for y in range(grid_length):
            if source_grid[x][y] < 90:
                line.append(SEA)
            elif source_grid[x][y] < 100:
                line.append(DENSELY_POPULATED)
            elif source_grid[x][y] < 120:
                line.append(MODERATELY_POPULATED)
            elif source_grid[x][y] < 140:
                line.append(LOSELY_POPULATED)
            elif source_grid[x][y] < 180:
                line.append(DESERT)
            elif source_grid[x][y] < 200:
                line.append(LOSELY_POPULATED)
            else:
                line.append(MOUNTAIN)
        result.append(line)
    return result


'''
This function projects the source_grid into another grid where each color
is mapped to another color
'''
##def to_refined_type_old(source_grid):
##    result= []
##    grid_length = len(source_grid)
##    for x in range(grid_length):
##        line = []
##        for y in range(grid_length):
##            if source_grid[x][y] < 120:
##                line.append(SEA)
##            elif source_grid[x][y] < 130:
##                line.append(DENSELY_POPULATED)
##            elif source_grid[x][y] < 150:
##                line.append(MODERATELY_POPULATED)
##            elif source_grid[x][y] < 185:
##                line.append(LOSELY_POPULATED)
##            elif source_grid[x][y] < 200:
##                line.append(DESERT)
##            else:
##                line.append(MOUNTAIN)
##        result.append(line)
##    return result

'''
This function converts a colored grid into an elevation_for_population_seed grid
used to initialise the population seeds
Each box of an elevation_for_population grid is valued at
0 if cannot be populated (river / mountain / desert)
1 if losely populated
2 if moderately populated
4 if densely populated
'''
def to_elevation_for_population_seed(source_grid):
    result = []
    grid_length = len(source_grid)
    for x in range(grid_length):
        line = []
        for y in range(grid_length):
            if source_grid[x][y] == DENSELY_POPULATED:
                line.append(PROB_DENSELY)
            elif source_grid[x][y] == MODERATELY_POPULATED:
                line.append(PROB_MODERATELY)
            elif source_grid[x][y] == LOSELY_POPULATED:
                line.append(PROB_LOSELY)
            else:
                line.append(PROB_NO_POPULATION)
        result.append(line)
    return result

'''
This function converts a colored grid into an elevation_for_population_iterate grid
used to iterate and make the population grow
Each box of an elevation_for_population grid is valued at
0 if cannot be populated (river / mountain)
1 if desert
2 if losely populated
4 if moderately populated
8 if densely populated
'''
def to_elevation_for_population_iterate(source_grid):
    result = []
    grid_length = len(source_grid)
    for x in range(grid_length):
        line = []
        for y in range(grid_length):
            if source_grid[x][y] == DENSELY_POPULATED:
                line.append(PROB_DENSELY_ITERATE)
            elif source_grid[x][y] == MODERATELY_POPULATED:
                line.append(PROB_MODERATELY_ITERATE)
            elif source_grid[x][y] == LOSELY_POPULATED:
                line.append(PROB_LOSELY_ITERATE)
            elif source_grid[x][y] == DESERT:
                line.append(PROB_DESERT_ITERATE)
            else:
                line.append(PROB_NO_POPULATION)
        result.append(line)
    return result

def population_density_number_to_color(population_count, max_pop_per_box):
    # color will range from 0 to 100 by steps depending on max_pop_per_box
    # 0 is max_pop_per_box people, 100 is 1 people
    scaled_population_count = (population_count * 180) // max_pop_per_box
    
    return 180 - scaled_population_count

'''
Temporary: put someone in source_grid where there is someone (given by population_grid)
'''
def merge_elevation_with_population(source_grid, population_grid, max_pop_per_box):
    result = []
    grid_length = len(source_grid)
    for x in range(grid_length):
        line = []
        for y in range(grid_length):
            if (population_grid[x][y] == 0):
                line.append(source_grid[x][y])
            else:
                color_number = population_density_number_to_color(population_grid[x][y], max_pop_per_box)
                color = []
                color.append(color_number)
                color.append(color_number)
                color.append(color_number)
                line.append(color)
        result.append(line)
    return result

'''
This function maps a colored_grid to a True-False grid stating
whether an antenna can be deployed or not.
An antenna cannot be deployed iff it is SEA or MOUNTAIN
'''
def antenna_deployment_candidates(colored_grid_no_population):
    result= []
    grid_length = len(colored_grid_no_population)
    for x in range(grid_length):
        line = []
        for y in range(grid_length):
            if colored_grid_no_population[x][y] in (MOUNTAIN, SEA):
                line.append(False)
            else:
                line.append(True)
        result.append(line)
    return result

            









