import operator
import numpy as np

from selections.selection_helper import correct_population


class TournamentSelection:
    @staticmethod
    def select(results, group_size, pop_size, population):
        winners = []
        while len(winners) < pop_size:
            results_1 = dict()
            for _ in range(group_size):
                rand_x = np.random.randint(0, pop_size)
                results_1[rand_x] = results[rand_x]
            point = population[min(results_1.items(), key=operator.itemgetter(1))[0]]

            winners.append(point)
        return correct_population(winners, population)
