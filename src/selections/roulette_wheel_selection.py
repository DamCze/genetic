import numpy as np

from selections.selection_helper import correct_population


class RouletteWheelSelection:
    @staticmethod
    def select(results, pop_size, population):
        winners = correct_population(population)
        new_results = [1 / i if i != 0 else 1 / i + 1 for i in results]
        sum_of_results = sum(new_results)
        probability_list = RouletteWheelSelection._probability_of_choice(sum_of_results, new_results)
        cumulative_distribution = RouletteWheelSelection._set_up_cumulative_distribution(probability_list)
        while len(winners) < pop_size:
            point = RouletteWheelSelection._spin_roulette(cumulative_distribution, population)
            winners.append(point)
        return winners

    @staticmethod
    def _probability_of_choice(_sum_of_results, _results):
        _probability_list = []
        for i in _results:
            _probability = i / _sum_of_results
            _probability_list.append(_probability)
            return _probability_list

    @staticmethod
    def _set_up_cumulative_distribution(_probability_list):
        _cumulative_distribution = []
        for i in range(len(_probability_list)):
            _sum = 0
            for j in range(i + 1):
                _sum += _probability_list[j]
            _cumulative_distribution.insert(i, _sum)
        return _cumulative_distribution

    @staticmethod
    def _spin_roulette(_cumulative_distribution, _population):
        random_num = np.random.random()
        index = len(_cumulative_distribution) - 1

        for i in range(len(_cumulative_distribution)):
            if random_num <= _cumulative_distribution[i]:
                index = i
                break
        return _population[index]
