# kidneyx
Generates a random digraph to represent a simplified version of the kidney exchange problem, and then attempts to find a good solution using Integer Linear Programming.

Based off: [Abraham, Blum and Sandholm (2007)](http://www.cs.cmu.edu/~dabraham/papers/abs07.pdf)

Each node represents a donor-recipient pair with incompatible blood types, and an edge a -> b will only be made if donor a has the same blood type as recipient b.
Each edge is assigned a random 'quality' weighting from 1 to 100.

The algorithm finds disjoint cycles in the graph, attempting to perform as many exchanges as possible and maximise the total weight of the cycles. 

# Run
* Ensure you have networkx 2 and matplotlib installed.
* Run ```python ilp.py -s n k``` where n is the number of vertices, k is the maximum cycle length, and omitting -s will show a plot of the graph generated.
# 

# To Do
* Add altruistic donors, so both cycles and chains can be searched for
