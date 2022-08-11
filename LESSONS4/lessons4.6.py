from itertools import count, cycle

for n in count(3):
    if n > 10:
        break
    else:
        print(n)

x = 0
for i in cycle("QWERTY"):
    if x > 10:
        break
    else:
        print(i)
        x += 1
