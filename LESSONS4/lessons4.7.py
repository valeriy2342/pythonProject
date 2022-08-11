def function(n):
    x = 1
    for i in range(n + 1):
        yield f'{i} = {x}'
        x *= i + 1


for y in function(4):
    print(y)
