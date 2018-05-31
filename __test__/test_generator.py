# generator test

def squares(n = 10):
    # data = [x**2 for x in range(n)]
    # return data
    for i in range(n):
        yield (i, i**2)


for x in squares(20):
    print(x)
