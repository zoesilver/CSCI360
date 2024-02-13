from lab1_utils import TextbookStack, apply_sequence
from lab1 import breadth_first_search, depth_first_search
from itertools import permutations
from itertools import product
from typing import List

nVals = [1,2,3, 4]
# nVals: List[int] = [1, 2, 3]
BFflipav = []
BFnodeav = []
DFflipav = []
DFnodeav = []
for n in nVals:
    initial_order = list(permutations(range(n)))
    IOsize = 0
    numFlipsBF =0
    numFlipsDF=0
    for perm in initial_order:
        combinations = list(product([0, 1], repeat=n))
        for combo in combinations:
            test = TextbookStack(perm, combo)
            test2 = TextbookStack(perm, combo)
            sequence = breadth_first_search(test)
            sequence2 = depth_first_search(test2)
            numFlipsBF += len(sequence)
            numFlipsDF+= len(sequence2)
            IOsize=IOsize+1

    averageBFflips = numFlipsBF/IOsize
    averageBFnodes= (numFlipsBF+1)/IOsize
    averageDFflips = numFlipsDF/IOsize
    averageDFnodes= (numFlipsDF+1)/IOsize

    BFflipav.append(averageBFflips)
    BFnodeav.append(averageBFnodes)
    DFflipav.append(averageDFflips)
    DFnodeav.append(averageDFnodes)

for x in range(5):
    print("n = ",x," BFS average flips:", BFflipav[x-1])
    print("n = ",x," BFS average nodes seen:", BFnodeav[x-1])
    print("n = ",x," DFS average flips:", DFflipav[x-1])
    print("n = ",x," DFS average nodes seen:", DFnodeav[x-1])
    print()

