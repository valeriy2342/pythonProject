my_list = list(range(20, 241))
new_list = [n for n in my_list if n % 20 == 0 or n % 21 == 0]
print(new_list)
