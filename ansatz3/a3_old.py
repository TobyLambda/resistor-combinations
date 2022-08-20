import itertools
from pprint import pprint

from COMB_base import COMBS

# # Generation # # =========================
# alle möglichkeiten                        x
# 4. zahl hinzufügen 0 - N-1                x
# >> lines                                  x
# alle kombinationen                        x
# >> grids                                  x

# # Prüfung # # ===========================
# dif 2-3 = 0                               x
# z4 = 0 >> z2 & z3 = 0                     x
# z2 <= sum(z3) - z3                           x
# z3 <= sum(z2) - z2                           x
# sum(z1) >= 2                                 x
# z4 <= sum(z4) - z4                           x
# sum(z2) % 2 = 0 | sum(z3) % 2 = 0            x
# sum(z4) >> z2 > 0 AND z3 > 0                 x
# min 50%: z2 == 2 || z3 == 2 >> z1 == 0       x  
# not z2[i] == z2[i] == z3[1] == z3[2] == 1    x  

N = 3

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
    # dif z2 - z3 = 0 || CHECK 1
    z1, z2, z3, z4 = 0, 0, 0, 0
    for line in grid:
        z1 += line[0]; z2 += line[1]; z3 += line[2]; z4 += line[3]
    if not z2 - z3 == 0: continue
    # z4 = 0 >> z2 & z3 = 0 || CHECK 2
    for line in grid:
        if line[3] != 0: continue
        if line[1] != 0 or line[2] != 0: break
    else: # || CHECK 3
        for line in grid:
            if not line[1] <= z3 - line[2]: break # z2 <= sum(z3) - z3
            if not line[2] <= z2 - line[1]: break # z3 <= sum(z2) - z2
            if not z1*2 >= 2: break # sum(z1) >= 2
            if not line[3] <= z4 - line[3]: break # z4 <= sum(z4) - z4
            if not z2 % 2 == 0 or not z3 % 2 == 0: break # sum(z2) % 2 = 0 | sum(z3) % 2 = 0
            if z4 > 0 and (z2 == 0 and z3 == 0): break # sum(z4) >> z2 > 0 AND z3 > 0
        else: # || CHECK 4
            broken_lines = 0
            for line in grid:
                if line[1] == 2 or line[2] == 2 and line[0] != 0: broken_lines += 1
            if broken_lines > (len(grid)/2): continue
            else: # || CHECK 5, not z2[1] == z2[2] == z3[1] == z3[2] == 1
                is_1 = False
                for line in grid:
                    if line[1] == line[2] == 1:
                        if is_1 == True: break
                        else: is_1 = True
                else: POSSIBLE_GRIDS.append(grid)
    
pprint(POSSIBLE_GRIDS)

print("original", len(GRIDS))
print("possible", len(POSSIBLE_GRIDS))
with open("test.txt", "w") as f: f.write(str(POSSIBLE_GRIDS))



        

