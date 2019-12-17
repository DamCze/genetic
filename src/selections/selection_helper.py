from typing import List
from utils import check_if_even

import numpy as np


def correct_population(_winners, _population) -> List:
    if not check_if_even(len(_winners)):
        rand_x = np.random.randint(0, len(_population))
        # return [_population[rand_x]]
        return [*_winners, _population[rand_x]]
    return _winners
