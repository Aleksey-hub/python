# Начните работу над проектом «Склад оргтехники». Создайте класс,
# описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Warehouse:
    def __init__(self, product_description, count):
        self.product_description = product_description  # Описание товара (наименование, модель...)
        self.count = count  # Количество на складе


class OfficeEquipment:
    def __init__(self, name_model, weight):
        self.name_model = name_model
        self.weight = weight  # Вес


class Printer(OfficeEquipment):
    def __init__(self, name_model, weight, printing_speed, cartridge_resource):
        super().__init__(self, name_model, weight)
        self.printing_speed = printing_speed
        self.cartridge_resource = cartridge_resource


class Scanner(OfficeEquipment):
    def __init__(self, name_model, weight, dpi):
        super().__init__(self, name_model, weight)
        self.dpi = dpi


class Xerox(OfficeEquipment):
    def __init__(self, name_model, weight, printing_speed, cartridge_resource, dpi):
        super().__init__(self, name_model, weight)
        self.printing_speed = printing_speed
        self.cartridge_resource = cartridge_resource
        self.dpi = dpi
