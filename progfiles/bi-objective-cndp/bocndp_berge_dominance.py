class BergeDominance(Dominance):
    def __init__(self):
        super(BergeDominance, self).__init__()

    def compare(self, x, y):
        b_x = 0
        b_y = 0

        nodes_x = x.variables[0][:]
        nodes_y = y.variables[0][:]

        H_x = x.objectives[0]
        H_y = y.objectives[0]

        var_H_x = x.objectives[1]
        var_H_y = y.objectives[1]

        for i in range(k):
            tmp        = nodes_y[i]
            nodes_y[i] = nodes_x[i]

            if connected_components(nodes_y) > H_x:     b_x += 1
            if cardinality_variance(nodes_y) < var_H_x: b_x += 1

            nodes_y[i] = tmp

        for i in range(k):
            tmp        = nodes_x[i]
            nodes_x[i] = nodes_y[i]

            if connected_components(nodes_x) > H_y:     b_y += 1
            if cardinality_variance(nodes_x) < var_H_y: b_y += 1

            nodes_x[i] = tmp

        if   b_x < b_y: return -1
        elif b_x > b_y: return  1
        else          : return  0
