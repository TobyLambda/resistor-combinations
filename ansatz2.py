from turtle import position
import numpy as np
import itertools, more_itertools, time, os, math
from pprint import pprint
from utils import render_grid

## GENERATE CIRCUIT GRIDS

start_t = time.time()

def generate_grids(total_resistors: int):
    # # # compute grid size
    # grid size is the maximum amount of space thats needed to fit all combinations
    # danke Jurek <3
    tr = total_resistors
    #xy = math.ceil(((tr**2)+tr)/4) # (n^2 + n) / 4
    xy = tr
    dim = xy**2 # x * y

    # # # generate gridlines
    gridlines = []
    i = 0
    for pos in more_itertools.distinct_combinations(range(dim), tr):
        base = [0 for _ in range(dim)]
        for p in pos:
            base[p] = 1
        gridlines.append(base)
    global end_t; end_t = time.time()
    pprint(gridlines)

    """
    ANSATZ SCHEITERT AN RECHNUNG
    """





   
def get_grid_value(grid: list, v: int = 2):
    # convert grid
    grid = np.array(grid).T.tolist()
    # initialize variables
    height = len(grid); width = len(grid[0]); value = 0

    for r in grid:
        for i, p in enumerate(r):
            if p == 0: r[i] = None
            if p == 1: r[i] = True

    for row_index, row in enumerate(grid):
        r_count = 0
        for p in row:
            if not p == None: r_count += 1
        if r_count == 0: continue # empty row
        elif r_count == 1: value += v # row with one resistor
        else: # row with more than one resistor (parallel)
            for i, p in enumerate(row): # go trough row positions
                if not p: continue # pos = false
                parallels = 0 # number of resistors in that row
                for ri, row in enumerate(grid):
                    if not ri >= row_index: continue
                    if row[i]: 
                        parallels += 1 # add one to parallels if there is resistor on same pos
                        row[i] = False # indicate resitor was used
                    else: break
                row_val = 1/(parallels*v)
                value += row_val
    return value
                    

class Grid:
    def __init__(self, l) -> None:
        self.l = l
        self.v = get_grid_value(self.l)

RESISTORS = 6

grids = generate_grids(RESISTORS)
print(f"time: {end_t - start_t}")



"""for _ in range(len(grids)):
    g = Grid(grids.pop())
    grids = [g] + grids

# # # filter unique grids
know_values = []
unique_grids = []
for g in grids:
    if not g.v in know_values:
        know_values.append(g.v)
        unique_grids.append(g)

end_t = time.time()


# # # render grids
os.system("clear")

for g in grids:
    render_grid(g)

print()
print("==================")
print()

for g in unique_grids:
    render_grid(g)

print(f"amount of resistors: {RESISTORS}")
print(f"(total grids: {len(grids)})")
print(f"total unique grids: {len(unique_grids)}")

print(f"execution time: {round(end_t - start_t, 3)}s")
input("...")"""
        
    
