class NashDominance(Dominance):
    def __init__(self):
        super(NashDominance, self).__init__()

    def compare(self, x, y):
        k_x = 0
        k_y = 0

        nodes_x = x.variables[0][:]
        nodes_y = y.variables[0][:]

        H_x = x.objectives[0]
        H_y = y.objectives[0]

        var_H_x = x.objectives[1]
        var_H_y = y.objectives[1]

        for i in range(k):
            tmp        = nodes_x[i]
            nodes_x[i] = nodes_y[i]

            if connected_components(nodes_x) > H_x:     k_x += 1
            if cardinality_variance(nodes_x) < var_H_x: k_x += 1

            nodes_x[i] = tmp

        for i in range(k):
            tmp        = nodes_y[i]
            nodes_y[i] = nodes_x[i]

            if connected_components(nodes_y) > H_y:     k_y += 1
            if cardinality_variance(nodes_y) < var_H_y: k_y += 1

            nodes_y[i] = tmp

        if   k_x < k_y: return -1
        elif k_x > k_y: return  1
        else          : return  0
