import numpy as np


class BestSelection:
    @staticmethod
    def select(results, percent_best, pop_size, population):
        winners = []

        ix = 0
        number_of_best = round(percent_best * len(results))
        while ix < number_of_best:
            ix += 1
            point_1 = population[results.index(min(results))]
            results[results.index(min(results))] = max(results)
            point_2 = population[results.index(min(results))]
            # results[results.index(min(results))] = max(results)  # sprawdzic
            winners.append((point_1, point_2))

            while len(winners) < pop_size:
                rand_x_1 = np.random.randint(0, pop_size)
                point_1 = population[rand_x_1]

                rand_x_2 = np.random.randint(0, pop_size)
                point_2 = population[rand_x_2]

                winners.append((point_1, point_2))
            return winners
