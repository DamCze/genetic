from typing import List
from utils import check_if_even

import numpy as np


def correct_population(_population) -> List:
    if not check_if_even(len(_population)):
        rand_x = np.random.randint(0, len(_population))
        return [_population[rand_x]]
    return []
