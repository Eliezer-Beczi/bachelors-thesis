def genetic_algorithm(G, k, N=30, pi_min=5, pi_max=50, delta_pi=5, alpha=0.2, tmax=1000):
    def fitness_function(S):
        subgraph = networkx.subgraph_view(G, filter_node=lambda n: n not in S)
        metric = connectivity_metric.pairwise_connectivity(subgraph)
        commonalities = S.intersection(best_S)

        return metric + gamma * len(commonalities)

    def my_cmp(a, b):
        return fitness_function(a) - fitness_function(b)

    t = 0
    P = []
    pi = pi_min
    my_key = functools.cmp_to_key(my_cmp)

    while len(P) < N:
        P.append(generate_random_solution(G, k))

    best_S = P[0].copy()
    gamma = update(G, best_S, P, alpha)
    best_S_fitness = fitness_function(best_S)

    while t < tmax:
        new_P = new_generation(k, N, P)
        mutation(G, k, N, new_P, pi)

        P.extend(new_P)
        P.sort(key=my_key)
        P = P[:N]

        curr_S = P[0]
        curr_S_fitness = fitness_function(curr_S)

        if curr_S_fitness < best_S_fitness:
            best_S = curr_S.copy()
            best_S_fitness = curr_S_fitness
            pi = pi_min
        else:
            pi = min(pi + delta_pi, pi_max)

        gamma = update(G, best_S, P, alpha)
        t += 1

    return best_S, best_S_fitness
