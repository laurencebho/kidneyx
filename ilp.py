import networkx as nx
import matplotlib.pyplot as plt
import argparse
import gen
import sys

def all_cycles(k, G):
    all_cycles = list(nx.simple_cycles(G))
    valid_cycles = []
    for c in all_cycles:
        if len(c) <= k:
            valid_cycles.append(c)
    return valid_cycles

def gen_matrix(cycles, n):
    M = []
    for c in cycles:
        row = [0] * n
        for node in c:
            row[node - 1] = 1
        M.append(row)
    return M

def weight(cycle, G):
    weight = 0
    for i in range(len(cycle) - 1):
        weight += G.edges[cycle[i], cycle[i+1]]['weight']
    return weight

def find_best_cycle(node, M, weights, current_cycles):
    best_weight = 0
    best = None
    for i, row in enumerate(M):
        if row[node - 1] == 1 and is_disjoint(row, M, current_cycles) and weights[i] > best_weight:
            best = i
            best_weight = weights[i]
    return best

#check if a cycle is disjoint from an existing array of cycles
def is_disjoint(row, M, cycles):
    for i, b in enumerate(row):
        if b == 1:
            for c in cycles:
                if c is not None:
                    if M[c][i] == 1:
                        return False
    return True

def greedy_solve(k, G, n):
    cycle_paths = all_cycles(k, G)
    M = gen_matrix(cycle_paths, n)
    cycles = []
    weights = [weight(path, G) for path in cycle_paths]
    for i in range(n):
        node_best = find_best_cycle(i+1, M, weights, cycles)
        cycles.append(node_best)
    display_result(cycles, cycle_paths, n)

    print('Total weight: {weight}'.format(weight=sum([weight(cycle_paths[i], G) for i in cycles if i is not None])))

def display_result(cycles, paths, n):
    exchanges = 0
    print('Cycles:')
    for i in cycles:
        if i is not None:
            cycle_str = ''
            for node in paths[i]:
                cycle_str += '-' + str(node) + '-'
                exchanges += 1
            cycle_str += '>'
            print(cycle_str)

    print('Exchanges made: {exchanges} out of a possible {n}'.format(exchanges=exchanges, n=n))
                
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--show", action="store_true")
    parser.add_argument("n", type=int)
    parser.add_argument("k", type=int)
    args = parser.parse_args()
    G = gen.random_graph_no_alts(args.n)
    if args.show:
        nx.draw(G)
        plt.show()
    greedy_solve(args.k, G, args.n)

if __name__ == "__main__":
    main() 
