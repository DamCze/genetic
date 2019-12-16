import numpy as np
from utils import check_if_mutate


class ArithmeticCrossover:
    def __init__(self, crossover_probability: float) -> None:
        self.crossover_probability = crossover_probability

    def cross(self, x_1, x_2, y_1, y_2):
        if check_if_mutate(self.crossover_probability):
            k = np.random.rand()
            x_1_new = k * x_1 + (1 - k) * x_2
            y_1_new = k * y_1 + (1 - k) * y_2
            x_2_new = (1 - k) * x_1 + k * x_2
            y_2_new = (1 - k) * y_1 + k * y_2
            return x_1_new, x_2_new, y_1_new, y_2_new
        return x_1, x_2, y_1, y_2
