def calc(lit):
    p = 1
    for x in lit:
        for y in x:
            p *= int( 441`y)
    return p

print(calc([[1,2], [3,4], [5,6,7]]))
