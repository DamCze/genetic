import numpy as np

from selections import *
from strategies import *


class Genetic:
    def __init__(self, f, selection_type, pop_size=100, n_variables=2, elite_strategy_size=1, percent_best=0.1,
                 group_size=3):
        self.f = f
        self.pop_size = pop_size
        self.selection_type = selection_type
        self.n_variables = n_variables
        self.minimum = -4.5
        self.maximum = 4.5
        self.percent_best = percent_best
        self.population = self.initialize_population()
        self.strategy_provider = EliteStrategy(elite_strategy_size)
        self.group_size = group_size
        self.offsprings = []

    def initialize_population(self):
        return [np.random.uniform(self.minimum, self.maximum, size=self.n_variables) for _ in range(self.pop_size)]

    def evaluate_population(self):
        return [self.f(i[0], i[1]) for i in self.population]

    def make_selection(self):
        results = self.evaluate_population()
        self.offsprings = self.strategy_provider.use_strategy(self.population, results)
        winners = self.set_up_selection(results)
        return winners

    def make_crossover(self):
        pass

    def set_up_selection(self, results):
        if self.selection_type == ITournamentSelection:
            return TournamentSelection.select(results, self.group_size, self.pop_size, self.population)
        elif self.selection_type == IBestSelection:
            return BestSelection.select(results, self.percent_best, self.pop_size, self.population)
        elif self.selection_type == IRouletteWheelSelection:
            return RouletteWheelSelection.select(results, self.pop_size, self.population)

    def print_population(self):
        print(self.population)
