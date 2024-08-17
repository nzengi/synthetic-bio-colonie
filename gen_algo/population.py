import numpy as np

class Population:
    def __init__(self, size, gene_length):
        self.size = size
        self.gene_length = gene_length
        self.individuals = self._initialize_population()

    def _initialize_population(self):
        return np.random.randint(0, 2, (self.size, self.gene_length))

    def get_individuals(self):
        return self.individuals
