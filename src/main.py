from genetic import Genetic
from crossovers import *
from mutations import *
from selections import *

f = lambda x, y: ((1.5 - x + x * y) ** 2 + (2.25 - x + x * y ** 2) ** 2 + (2.625 - x + x * y ** 3) ** 2)

iterations = 100

# region Initialize mutations
regular_mutation = RegularMutation(1)
index_change_mutation = IndexChangeMutation(1)
# endregion

# region Initialize crossovers
arithmetic_crossover = ArithmeticCrossover(1)
heuristic_crossover = HeuristicCrossover(1, 5, arithmetic_crossover)
# endregion

genetic = Genetic(f, ITournamentSelection, index_change_mutation, heuristic_crossover)

for _ in range(iterations):
    winners = genetic.make_selection()
    genetic.make_crossover(winners)
