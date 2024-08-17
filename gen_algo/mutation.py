import numpy as np

class Mutation:
    @staticmethod
    def mutate(individual, mutation_rate=0.01):
        for i in range(len(individual)):
            if np.random.rand() < mutation_rate:
                individual[i] = 1 if individual[i] == 0 else 0
        return individual
