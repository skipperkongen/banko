import random

class Algorithm2:

    def __init__(self, seed):
        self.rng = random.Random(seed)

    def generate(self):
        # first, generate full plate
        cols = [
            self._generate_full_col(col)
            for col in range(9)
        ]
        # second, delete four values per row, keeping at least one value per column
        plate = self._eliminate(cols)
        return plate

    def _generate_full_col(self, col):
        max_num = 11 if col == 8 else 10
        return [
            x+col*10 for x
            in sorted(self.rng.sample(range(max_num), k=3))
        ]

    def _eliminate(self, cols):
        first_two = [self.rng.sample(range(9), k=4) for _ in range(2)]
        tabu = [i for i in range(9) if i in first_two[0] and i in first_two[1]]
        third = self.rng.sample([i for i in range(9) if i not in tabu], k=4)
        deletions = [first_two[0], first_two[1], third]
        # transpose columns for easier deletion
        rows = [list(x) for x in zip(*cols)]
        for ds, row in zip(deletions, rows):
            for d in ds:
                row[d] = None
        return rows

if __name__=='__main__':
    algo = Algorithm2(42)
    plate = algo.generate()
    for row in plate:
        print(row)
