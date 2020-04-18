def update(G, best_S, P, alpha):
    subgraph = networkx.subgraph_view(G, filter_node=lambda n: n not in best_S)
    metric = connectivity_metric.pairwise_connectivity(subgraph)
    avg = 0

    for S in P:
        avg += len(S.intersection(best_S))

    avg /= len(P)
    return float('inf') if avg == 0 else (alpha * metric) / avg
