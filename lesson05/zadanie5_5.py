# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('text5_5.txt', 'w') as f:
    f.write('5 10 25 20 15 25')

with open('text5_5.txt', 'r') as f:
    my_str = f.read()
    my_str = my_str.split(' ')
    sum = 0
    for num in my_str:
        sum += int(num)
    print(f'Сумма чисел равна: {sum}')