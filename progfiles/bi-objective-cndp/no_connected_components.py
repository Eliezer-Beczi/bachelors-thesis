def connected_components(exclude=None):
    if exclude is None:
        exclude = {}

    S = set(exclude)
    subgraph = networkx.subgraph_view(G, filter_node=lambda n: n not in S)
    return networkx.number_connected_components(subgraph)
