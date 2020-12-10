from advent import AdventAPI

class BoardingTree():
    def __init__(self, values):
        half = int(len(values) / 2)
        self.value = values[half]
        if half > 0:
            self.higher = BoardingTree(values[half:])
            self.lower = BoardingTree(values[:half])
        else:
            self.lower = self.higher = None

    def traverse(self, instructions):
        if len(instructions) == 0:
            return self.value
        else:
            instr = instructions[0]
            if instr in ['F', 'L'] and self.lower:
                return self.lower.traverse(instructions[1:])
            if instr in ['B', 'R'] and self.higher:
                return self.higher.traverse(instructions[1:])

    def __str__(self):

        return '(Tree v: {}, l: {}, h: {})'.format(self.value, self.lower, self.higher)


row = BoardingTree(list(range(128)))
column = BoardingTree(list(range(8)))

a = AdventAPI()
input = a.get_input(5).decode().split()
result = [ 
    row.traverse(i[:7]) * 8 + column.traverse(i[-3:])
    for i in input
]
result.sort()
max_seat = max(result)
min_seat = min(result)
my_seat = [
    seat
    for seat in range(min_seat, max_seat)
    if not seat in result
]
print(my_seat)
print(max(result))
