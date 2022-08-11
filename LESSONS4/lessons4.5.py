from functools import reduce

my_list = list(range(100, 1001))
list1 = [n for n in my_list if n % 2 == 0]
new_list = [reduce(lambda x, y: x * y, list1)]
print(new_list)
print(list1)
