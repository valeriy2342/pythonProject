with open("text_1.txt", 'w', encoding="utf-8") as f:
    while True:
        text = input("Введите текст: ")
        if text == '':
            if not text:
                break
        print(text, file=f)


text_file = open("text_1.txt", 'r', encoding="utf-8")
new_text = text_file.readlines()
print(f'Количество строк в файле - {len(new_text)}')

for i in range(len(new_text)):
    print(f'Окличество символов {i + 1} - ой строки {len(new_text[i])}')
my_file = open("text_1.txt", 'r', encoding="utf-8")
new_text = my_file.read()
new_text = new_text.split()
print(f'Общее количество слов - {len(new_text)}')
text_file.close()