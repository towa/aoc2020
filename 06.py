from advent import AdventAPI
from functools import reduce

a = AdventAPI()

input = a.get_input(6).decode().split('\n\n')

result_a = [
    len(list(set([
        q 
        for q in list(group)
        if q != '\n'
    ])))
    for group in input
]

print(sum(result_a))

def everyone(group):
    all_answers = list(set([
        q
        for q in list(group)
    ]))
    return list(filter(
        lambda x: reduce(lambda a,b: a and b,
            [x in p for p in group.split()]),
        all_answers
    ))

result_b = [
    len(everyone(group))
    for group in input
]
print(sum(result_b))