# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyZeroDivision(Exception):
    def __str__(self):
       return 'На ноль делить нельзя!'

num_1 = input('Введите 1-е число: ')
num_2 = input('Введите 2-е число: ')

try:
    num_1 = int(num_1)
    num_2 = int(num_2)

    if num_2 == 0:
        raise MyZeroDivision
    print(f'{num_1/ num_2}')
except ValueError:
    print('Введено не число!')
except MyZeroDivision as err:
    print(err)