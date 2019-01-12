import networkx as nx
import random

#pairs = number of incompatible donor-recipient pairs, alts = number of altruistic donors
def random_graph(pairs, alts):
    G = nx.DiGraph()
    add_random_nodes(pairs, alts, G)
    add_random_edges(G)
    return G

def random_graph_no_alts(pairs):
    return random_graph(pairs, 0)

def add_random_nodes(pairs, alts, G):
    types = ['O+', 'O-', 'B+', 'B-', 'A+', 'A-']
    for i in range(pairs):
        donor = random.choice(types)
        while True:
            recipient = random.choice(types)
            if recipient != donor:
                break

        G.add_node(i, alt=False, donor=donor, recipient=recipient)
    for i in range(pairs, pairs + alts):
        donor = random.choice(types)
        G.add_node(i, alt=True, donor=donor, recipient=None)

#adds all edges where there is compatibility, with random integer edge weights (quality ratings)
def add_random_edges(G):
    nodes = list(G.nodes(data=True))
    for i, a in enumerate(nodes):
        for j, b in enumerate(nodes[i+1:]):
            if a[1]['donor'] == b[1]['recipient']:
                G.add_edge(i, j+i+1, weight=random.randint(1, 100))
            if b[1]['donor'] == a[1]['recipient']:
                G.add_edge(j+i+1, i, weight=random.randint(1, 100))
