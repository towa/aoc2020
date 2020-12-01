# very stupid solution using no for loops :)
with open('input') as file:
    lines = [int(l) for l in file.readlines()]
    res = [
        l1 * l2 * l3
        for l1 in lines
        for l2 in lines
        for l3 in lines
        if l1 + l2 + l3 == 2020
    ].pop()
    print(res)