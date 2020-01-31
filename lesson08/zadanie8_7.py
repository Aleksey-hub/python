# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения
# и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение
# и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, num_complex):
        self.num_complex = num_complex

    def __str__(self):
        return str(self.num_complex)

    def __add__(self, other):
        return self.num_complex + other

    def __mul__(self, other):
        return self.num_complex * other


complex_number = ComplexNumber(complex(1, 5))
print(complex_number)
print(complex_number + complex(4, 5))
print(complex_number * complex(4, 5))
