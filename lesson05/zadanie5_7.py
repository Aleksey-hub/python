# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

with open('text5_7.txt', 'r') as f:
    firm_dict = {}
    sum_profit = 0
    count_profit_firm = 0
    for line in f:
        line = line.split(' ')
        profit = int(line[2]) - int(line[3])
        firm_dict[line[0]] = profit
        if profit >= 0:
            count_profit_firm += 1
            sum_profit += profit
    average_profit = {'average_profit': sum_profit / count_profit_firm}

    firm_list = []
    firm_list.append(firm_dict)
    firm_list.append(average_profit)
    print(firm_list)

with open('firm.json', 'w') as f:
    json.dump(firm_list, f)
