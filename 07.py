from advent import AdventAPI
from functools import reduce

class Bag():
    def __init__(self, instr_list, color):
        def parse_bag(bag):
            clr = ' '.join(bag.split()[1:3])
            number = int(bag.split()[0])
            return (number, Bag(instr_list, clr))

        instr = list(filter(
            lambda x: x.startswith(color),
            instr_list
        )).pop()
        split = instr.split(' bags contain ')
        self.color = split[0]
        self.children = []
        if split[1] != 'no other bags.':
            self.children = [
                parse_bag(bag)
                for bag in split[1].split(',')
            ]
    
    def __repr__(self):
        return '{} containing: {}'.format(self.color, self.children)

    def contains(self, color):
        if color == self.color:
            return True
        else:
            return reduce(
                lambda a, b: a or b,
                [
                    child[1].contains(color)
                    for child in self.children
                ],
                False)

    def count(self):
        if len(self.children) == 0:
            return 1
        else:
            return 1 + sum([
                b[1].count() * b[0]
                for b in self.children
            ])

        
a = AdventAPI()
input = a.get_input(7).decode().splitlines()

bags = [
    Bag(input, line.split(' bags')[0])
    for line in input
]
"""
bags_containing_gold = [
    b.color
    for b in bags
    if b.contains('shiny gold') and b.color != 'shiny gold'
]
print(len(bags_containing_gold))
"""

gold_bag = [
    b.count()
    for b in bags
    if b.color == 'shiny gold'
]
print(gold_bag[0] -1)