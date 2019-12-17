from crossovers import *
from genetic import Genetic
from mutations import *
from selections import *

f = lambda x, y: ((1.5 - x + x * y) ** 2 + (2.25 - x + x * y ** 2) ** 2 + (2.625 - x + x * y ** 3) ** 2)

regular_mutation = RegularMutation(1)
arithmetic_crossover = ArithmeticCrossover(1)

genetic = Genetic(f, ITournamentSelection, regular_mutation, arithmetic_crossover, pop_size=100)
winners = genetic.make_selection()
print(winners)
print(len(winners))
