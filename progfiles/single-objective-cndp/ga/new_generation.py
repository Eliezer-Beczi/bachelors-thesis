def new_generation(k, N, P):
    new_P = []

    for _ in range(N):
        r1 = random.randrange(N)
        r2 = random.randrange(N)

        while r1 == r2:
            r2 = random.randrange(N)

        new_S = P[r1].union(P[r2])

        if len(new_S) == k:
            new_P.append(new_S)
        else:
            tmp = list(new_S)
            random.shuffle(tmp)
            tmp = tmp[:k]

            new_P.append(set(tmp))

    return new_P
