import itertools
from pprint import pprint
from COMB_base import COMBS

# # Generation # # =========================
# alle möglichkeiten                    x
# 4. zahl hinzufügen 0 - N-1            x
# >> lines                              x
# alle kombinationen                    x
# >> grids                              x

# # Prüfung # # ===========================
# dif 2-3 = 0                           x
# z4 = 0 >> z2 & z3 = 0                 x
# z2 <= sum(z3) - z3                    x
# z3 <= sum(z2) - z2

N = 2

# # # generation
# # add fitht number to every line
COMBS5 = []
for fifth in range(0, N):
    for comb in COMBS:
        COMBS5.append(comb + [fifth])

# # combine every line to grid
GRIDS = list(itertools.combinations_with_replacement(COMBS5, N))

# # # checks
POSSIBLE_GRIDS = []
for grid in GRIDS:
    # dif z2 - z3 = 0
    z2, z3 = 0, 0
    for line in grid: z2 += line[1]; z3 += line[2]
    if not z2 - z3 == 0: continue
    # z4 = 0 >> z2 & z3 = 0
    for line in grid:
        if line[3] != 0: continue
        if line[1] != 0 or line[2] != 0: break
    else:
        # z2 <= sum(z3) - z3 ||| z3 <= sum(z2) - z2
        for line in grid:
            if not line[1] <= z3 - line[2]: break
            if not line[2] <= z2 - line[1]: break
        else: POSSIBLE_GRIDS.append(grid)
    
pprint(POSSIBLE_GRIDS)

print("original", len(GRIDS))
print("possible", len(POSSIBLE_GRIDS))



        

