class BOCNDP(Problem):
    def __init__(self):
        super(BOCNDP, self).__init__(nvars=1, nobjs=2)
        self.types[:] = Subset(list(G), k)
        self.directions[0] = Problem.MAXIMIZE
        self.directions[1] = Problem.MINIMIZE

    def evaluate(self, solution):
        S = solution.variables[0]
        solution.objectives[0] = connected_components(S)
        solution.objectives[1] = cardinality_variance(S)
