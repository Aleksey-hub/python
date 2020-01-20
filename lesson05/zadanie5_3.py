# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('text5_3.txt', 'r', encoding='utf-8') as f:
    my_dict = {}
    lines = f.readlines()
    for line in lines:
        line = line.split(' ')
        my_dict[line[0]] = int(line[1])
    # Определение сотрудников с окладом менее 20 тыс
    small_salary = ''
    for key, value in my_dict.items():
        if value < 20000:
            small_salary += key + ' '
    print(f'Оклад меньше 20000 имеют: {small_salary}')
    # Подсчет средней величины дохода сотрудников
    sum_salary = 0
    for value in my_dict.values():
        sum_salary += value
    average_salary = sum_salary / len(my_dict)
    print(f'Средний доход сотрудников составляет: {average_salary}')
