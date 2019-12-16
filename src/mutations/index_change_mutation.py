from utils import check_if_mutate


class IndexChangeMutation:
    def __init__(self, mutation_probability: float) -> None:
        self.mutation_probability = mutation_probability

    def mutate(self, x, y):
        if check_if_mutate(self.mutation_probability):
            return y, x
        return x, y
