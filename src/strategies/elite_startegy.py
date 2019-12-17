import numpy as np


class EliteStrategy:
    def __init__(self, number_of_individuals: int) -> None:
        self.number_of_individuals = number_of_individuals

    def use_strategy(self, _population, _results):
        _population_copy = _population.copy()
        _offsprings = []
        for _ in range(self.number_of_individuals):
            value = _population_copy[np.argmin(_results)]
            _offsprings.append(value)
        return _offsprings
