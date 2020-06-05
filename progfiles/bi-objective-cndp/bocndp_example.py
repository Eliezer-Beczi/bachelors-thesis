# define the problem definition
problem = BOCNDP()

# instantiate the optimization algorithm
algorithm = NSGAII(problem, selector=TournamentSelector(
    dominance=NashDominance()), archive=NashArchive())

# optimize the problem using 10,000 function evaluations
algorithm.run(10000)

# display the results
for solution in algorithm.result:
    print(solution.objectives)
