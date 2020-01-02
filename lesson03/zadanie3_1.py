# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return 'На ноль делить нельзя.'
    return result

print(division(10, 20))
print(division(10, 0))