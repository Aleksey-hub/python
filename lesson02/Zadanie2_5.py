# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
print(my_list)

new_element = int(input('Ведите новый элемент рейтинга: '))
if new_element in my_list:
    index = my_list.index(new_element)
    count = my_list.count(new_element)
    my_list.insert(index + count, new_element)
else:
    for i in range(0, len(my_list)):
        if new_element > my_list[i]:
            my_list.insert(i, new_element)
            break
    if new_element < my_list[len(my_list) - 1]:
        my_list.append(new_element)

print(my_list)