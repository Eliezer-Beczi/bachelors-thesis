def cardinality_variance(exclude=None):
    if exclude is None:
        exclude = {}

    S = set(exclude)
    subgraph = networkx.subgraph_view(G, filter_node=lambda n: n not in S)
    components = list(networkx.connected_components(subgraph))
    num_of_components = len(components)
    num_of_nodes = subgraph.number_of_nodes()
    variance = 0

    for component in components:
        cardinality = len(component)
        variance += (cardinality - num_of_nodes / num_of_components) ** 2

    variance /= num_of_components
    return variance
