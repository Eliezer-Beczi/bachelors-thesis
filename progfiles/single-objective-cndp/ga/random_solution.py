def generate_random_solution(G, k):
    S = list(G)

    while len(S) > k:
        S.pop(random.randrange(len(S)))

    return set(S)
