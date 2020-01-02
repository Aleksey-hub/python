# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(num1, num2, num3):
    my_list = [num1, num2, num3]
    my_list.sort(reverse=True)
    return my_list[0] + my_list[1]


print(my_func(10, 5, 15))
print(my_func(15, 5, 15))
