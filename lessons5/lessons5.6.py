def summa(file_path):
    result = {}
    try:
        with open(file_path, 'r') as f:
            for line in f:
                subject, numbers = line.split(':')
                subject_sum = sum(int(n) for word in numbers.split() for n in word.split('(') if n.isdigit())
                result[subject] = subject_sum
    except Exception as err:
        print('Ошибка :', err)
    return result


if __name__ == '__main__':
    from pprint import pprint
    res_dict = summa('text_6.txt')
    pprint(res_dict, width=1)