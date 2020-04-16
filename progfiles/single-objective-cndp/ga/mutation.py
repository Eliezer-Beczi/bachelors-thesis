def mutation(G, k, N, new_P, pi):
    for i in range(N):
        r = random.randint(1, 100)

        if r <= pi:
            new_S = list(new_P[i])
            ng = random.randint(0, k)
            random.shuffle(new_S)

            for _ in range(ng):
                new_S.pop()

            nodes = list(set(G) - set(new_S))
            random.shuffle(nodes)

            while len(new_S) < k:
                u = nodes.pop()
                new_S.append(u)
