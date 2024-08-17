class GeneticCircuit:
    def __init__(self, promoter, rbs, cds, terminator):
        self.promoter = promoter
        self.rbs = rbs
        self.cds = cds
        self.terminator = terminator

    def describe(self):
        return f"Promoter: {self.promoter}, RBS: {self.rbs}, CDS: {self.cds}, Terminator: {self.terminator}"
