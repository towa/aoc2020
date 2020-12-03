from functools import reduce

class TobogganMap():
    def __init__(self, mapfile):
        with open(mapfile) as input_file:
            lines = input_file.readlines()
        self.map = [line.rstrip() for line in lines]

    def __str__(self):
        return '\n'.join(self.map)

    def path(self, down, right):
        positions_down = range(0, len(self.map), down)
        positions_right = [
            (pos * right) % len(self.map[0])
            for pos in range(len(self.map))
        ]
        return zip(positions_down, positions_right)
    
    def count_trees(self, path):
        return sum([
            1
            for (down, right) in path
            if self.map[down][right] == '#'
        ])


tm = TobogganMap('input')

# part a
path = tm.path(1,3)
print(tm.count_trees(path))

# part b
counts = [
    tm.count_trees(tm.path(p[0], p[1]))
    for p in [(1,1), (1,3), (1,5), (1,7), (2,1)]
]
print(reduce(lambda x,y: x * y, counts))