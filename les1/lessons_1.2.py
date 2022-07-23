second = int(input('Введите время в секундах: '))
hour = second // 3600
hours = (hour) if hour > 10 else ('0' + str(hour))
minut = (second % 3600) // 60
minutes = (minut) if minut > 10 else ('0' + str(minut))
seconds = (second % 3600) % 60
res_seconds = (seconds) if seconds > 10 else ('0' + str(seconds))
if hour > 24:
    print('Количество полученных часов больше суток, повторите ввод.')
else:
    print(f'Ваше время: {hours}:{minutes}:{res_seconds}')
