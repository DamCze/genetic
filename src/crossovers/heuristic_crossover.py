import numpy as np
from utils import check_if_mutate


class HeuristicCrossover:
    def __init__(self, crossover_probability: float, attempts: int, crossover_alter) -> None:
        self.crossover_probability = crossover_probability
        self.attempts = attempts
        self.crossover_alter = crossover_alter

    def cross(self, x_1, x_2, y_1, y_2):
        if check_if_mutate(self.crossover_probability):
            for _ in range(self.attempts):
                if x_2 < x_1 and y_2 < y_1:
                    k_1 = np.random.rand()
                    x_1_new = k_1 * (x_2 - x_1) + x_2
                    y_1_new = k_1 * (y_2 - y_1) + y_2

                    k_2 = np.random.rand()
                    x_2_new = k_2 * (x_2 - x_1) + x_2
                    y_2_new = k_2 * (y_2 - y_1)
                    return x_1_new, x_2_new, y_1_new, y_2_new
            self.crossover_alter.cross(x_1, x_2, y_1, y_2)
        return x_1, x_2, y_1, y_2