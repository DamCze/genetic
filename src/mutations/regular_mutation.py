import numpy as np
from utils import check_if_mutate


class RegularMutation:
    def __init__(self, mutation_probability: float) -> None:
        self.mutation_probability = mutation_probability

    def mutate(self, x, y):
        if check_if_mutate(self.mutation_probability):
            selected_gene = np.random.choice([x, y])
            random_value = np.random.uniform(low=0, high=5)
            if selected_gene == x:
                return random_value, y
            else:
                return x, random_value
        return x, y
