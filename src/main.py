from genetic import Genetic

f = lambda x, y: ((1.5 - x + x * y) ** 2 + (2.25 - x + x * y ** 2) ** 2 + (2.625 - x + x * y ** 3) ** 2)

genetic = Genetic(f)
genetic.print_population()
