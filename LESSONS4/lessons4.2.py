my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [n for i, n in zip(my_list, my_list[1:]) if n > i]
print(new_list)
