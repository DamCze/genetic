import numpy as np


def check_if_mutate(_mutation_probability):
    rand_number = np.random.rand()
    return rand_number <= _mutation_probability
