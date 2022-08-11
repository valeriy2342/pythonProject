from sys import argv

name, time, in_an_hour, prize = argv

print(argv)
print(f'{(int(time) * int(in_an_hour)) + int(prize)} рублей')