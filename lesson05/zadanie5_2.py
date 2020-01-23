# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('text5_2.txt', 'r') as f:
    lines = f.readlines()
    print(f'Количество строк равно: {len(lines)}')
    for i, line in enumerate(lines, 1):
        print(f'В {i}-й строке {len(line.split(" "))} слов.')