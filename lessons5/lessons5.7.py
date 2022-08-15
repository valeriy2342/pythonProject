import json

with open("text_77.json", 'w', encoding="utf-8") as f:
    with open("text_7.txt", encoding="utf-8") as z:
        my_file = {i.split()[0]: int(i.split()[2]) - int(i.split()[3]) for i in z}
        new_file = [e for e in my_file.values() if e > 0]
        result = [my_file, {"Средняя прибыль ": round(sum(new_file) / len(new_file))}]

        json.dump(result, f, ensure_ascii=False, indent=4)
