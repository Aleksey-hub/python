# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open('text5_4.txt', 'r', encoding='utf-8') as f:
    my_str = ''
    for line in f:
        line = line.split(' ')
        if line[0] == 'One':
            line[0] = 'Один'
        elif line[0] == 'Two':
            line[0] = 'Два'
        elif line[0] == 'Three':
            line[0] = 'Три'
        elif line[0] == 'Four':
            line[0] = 'Четыре'
        my_str += ' '.join(line)
    print(my_str)

with open('text5_4(2).txt', 'w') as f:
    f.writelines(my_str)