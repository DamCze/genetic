import numpy as np
import operator


class TournamentSelection:
    @staticmethod
    def select(results, group_size, pop_size, population):
        winners = []
        while len(winners) < pop_size:
            results_1 = dict()
            for _ in range(group_size):
                rand_x = np.random.randint(0, pop_size)
                results_1[rand_x] = results[rand_x]
            point_1 = population[min(results_1.items(), key=operator.itemgetter(1))[0]]

            results_2 = dict()
            for _ in range(group_size):
                rand_x = np.random.randint(0, pop_size)
                results_2[rand_x] = results[rand_x]
            point_2 = population[min(results_2.items(), key=operator.itemgetter(1))[0]]
            winners.append((point_1, point_2))
        return winners
