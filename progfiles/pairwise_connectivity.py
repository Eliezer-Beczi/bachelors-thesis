def pairwise_connectivity(G):
    components = networkx.algorithms.components.connected_components(G)
    result = 0

    for component in components:
        n = len(component)
        result += (n * (n - 1)) // 2

    return result
