def greedy_cnp(G, k):
    S = networkx.algorithms.approximation.min_weighted_vertex_cover(G)

    while len(S) > k:
        B = objective_function.minimize_pairwise_connectivity(G, S)
        i = random.choice(B)
        S.discard(i)

    return S
