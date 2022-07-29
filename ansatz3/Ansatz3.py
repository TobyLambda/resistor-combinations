#Import same as Toby
import itertools, time, os, math
import more_itertools
import pprint 
from collections import OrderedDict
time_0 = time.time()

#Taking N as variable
#N=2


def combine(N):

    global lists
    global comb

    #All Combinations
    COMBS = [
        [1, 0, 0 ],
        [1, 0, 1 ],
        [1, 0, 2 ],
        [1, 1, 0 ],
        [1, 1, 1 ],
        [1, 1, 2 ],
        [1, 2, 0 ],
        [1, 2, 1 ],
        [1, 2, 2 ],
        [0, 1, 0 ],
        [0, 1, 1 ],
        [0, 1, 2 ],
        [0, 2, 0 ],
        [0, 2, 1 ],
        [0, 2, 2 ],
        [0, 0, 1 ],
        [0, 0, 2 ]
    ]   


    #Plus Z5 to every Combination
    lists = []
    rr = 0

    #ResetListen
    COMBSRES = []
    r = 0

    for i in range(0,N+1):
        COMBSRES.append( [
        [1, 0, 0 ],
        [1, 0, 1 ],
        [1, 0, 2 ],
        [1, 1, 0 ],
        [1, 1, 1 ],
        [1, 1, 2 ],
        [1, 2, 0 ],
        [1, 2, 1 ],
        [1, 2, 2 ],
        [0, 1, 0 ],
        [0, 1, 1 ],
        [0, 1, 2 ],
        [0, 2, 0 ],
        [0, 2, 1 ],
        [0, 2, 2 ],
        [0, 0, 1 ],
        [0, 0, 2 ]
        ] ) 
        rr += 1


    for i in range(0,N):
        for n in COMBS:
            n.append(i)
            lists.append(n)
        COMBS = COMBSRES[r]
        r += 1

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # IGNORE EVERYTHING ABOVE TO AVOID PERMANENT BRAIN DAMAGE # # #
    
    comb = list(itertools.combinations_with_replacement(lists, N))
    
    return comb


def check(comb):
    SumZ2, SumZ4 = 0, 0
    poss, imposs = [], []

    for n in comb:
        SumZ2, SumZ4 = 0, 0
        for x in n:
            SumZ2 = SumZ2 + x[1]
            SumZ4 = SumZ4 + x[2]
        #print (SumZ4 - SumZ2)
        if SumZ4 - SumZ2 == 0: poss.append(n)
        else: imposs.append(n)

    delete2 = []
    check2c = 0
    #pprint.pprint (poss)
    poss = poss + [[[0, 1, 1, 0], [0, 1, 1, 0]]] 
    poss2 = []
    for _ in range(len(poss)):
        grid = poss.pop()
        for line in grid:
            if line[3] == 0:
                if line[2] != 0 or line[1] != 0:
                    break
        else: poss2.append(grid)









    #pprint.pprint(poss)
    delete3 = []
    check3c = 0   
    for x in poss:
        SumZ4c, SumZ2c = 0, 0
        for n  in x:
            SumZ4c += n[2]
            SumZ2c += n[1]
            
        for n  in x:
            if n[1] > (SumZ4c - n[2]):
                delete3.append(check3c)
            else:
                if n[2] > (SumZ2c - n[1]):
                    delete3.append(check3c)
        check3c += 1
    delete3.sort(reverse=True)
    delete3 = list(OrderedDict.fromkeys(delete3))
    #print (len(poss))
    #print (delete3)
    for n3 in delete3:
        del poss[n3]



    
    return poss2




def run(N):
    poss = check(combine(N))

    print(len(lists))
    print(len(comb))
    print(len(poss))
    pprint.pprint (poss)



run(2)

pprint.pprint (comb)



















time_end = time.time()
print(time_end-time_0,"s")