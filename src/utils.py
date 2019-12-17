import numpy as np


def check_if_mutate(_mutation_probability: float) -> bool:
    rand_number = np.random.rand()
    return rand_number <= _mutation_probability


def check_if_even(_number: int) -> bool:
    return _number % 2 == 0
