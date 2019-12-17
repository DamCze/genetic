import numpy as np

from selections.selection_helper import correct_population


class BestSelection:
    @staticmethod
    def select(results, percent_best, pop_size, population):
        winners = correct_population(population)

        ix = 0
        number_of_best = round(percent_best * len(results))
        while ix < number_of_best:
            ix += 1
            point = population[results.index(min(results))]
            results[results.index(min(results))] = max(results)

            winners.append(point)

            while len(winners) < pop_size:
                rand_x = np.random.randint(0, pop_size)
                point = population[rand_x]

                winners.append(point)
            return winners
