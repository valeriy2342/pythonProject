with open("text_3.txt", 'r', encoding="utf-8") as my_file:
    my_list = {file.split()[0]: float(file.split()[1]) for file in my_file}
    print(f'Cредняя величина дохода всех сотрудников. = {round(sum(my_list.values()) / len(my_list), 3)} рублей\n'
          f'Сотрудники имеющие оклад менее 20 тысяч рублей {[e[0] for e in my_list.items() if e[1] < 20000]}')
