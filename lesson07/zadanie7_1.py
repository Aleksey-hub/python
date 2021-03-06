# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31  22
# 37  43
# 51  86
#
# 3  5  32
# 2  4  6
# -1 64 -8
#
# 3  5  8  3
# 8  3  7  1
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, list_matrix):
        self.list_matrix = list_matrix

    def __str__(self):
        for list in self.list_matrix:
            for el in list:
                print(el, end='\t')
            print('')

    def __add__(self, other):
        new_matrix = []
        for i, list in enumerate(self.list_matrix):
            new_list = []
            for j, el in enumerate(list):
                new_list.append(el + other[i][j])
            new_matrix.append(new_list)
        return new_matrix


my_matrix = Matrix([[1, 2, 3], [4, 5, 6]])
my_matrix.__str__()
print(my_matrix + [[10, 20, 30], [10, 20, 30]])
