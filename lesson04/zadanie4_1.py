# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
# платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах*ставка в
# час) + премия. Для выполнения расчета для конкретных значений необходимо запускать
# скрипт с параметрами.

from sys import argv


def wages(work_hour, money_hour, bonus):
    work_hour = float(work_hour)
    money_hour = float(money_hour)
    bonus = float(bonus)
    return work_hour * money_hour + bonus


params = argv
print(f'Заработная плата сотрудника: {wages(params[1], params[2], params[3])}')
