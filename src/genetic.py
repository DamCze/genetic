import numpy as np


class Genetic:
    def __init__(self, f, pop_size=100, n_variables=2):
        self.f = f
        self.pop_size = pop_size
        self.n_variables = n_variables
        self.minimum = -4.5
        self.maximum = 4.5
        self.population = self.initialize_population()
        self.offsprings = []

    def initialize_population(self):
        return [np.random.uniform(self.minimum, self.maximum, size=self.n_variables) for _ in range(self.pop_size)]

    def evaluate_population(self):
        return [self.f(i[0], i[1]) for i in self.population]

    def make_selection(self):
        pass

    def make_crossover(self):
        pass
