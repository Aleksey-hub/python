# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать
# в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class Warehouse:
    def __init__(self, product_description, count):
        if isinstance(count, int):
            self.product_list = [{'Описание товара': product_description, 'Количество на складе': count}]
        else:
            print('Введено некорректное количество.')

    def add_product(self, name, count):
        '''Добавление товара на склад'''
        if isinstance(count, int):
            for i, dict in enumerate(self.product_list):
                if name in dict.values():
                    self.product_list[i]['Количество на складе'] += count
                    break
            else:
                self.product_list.append({'Описание товара': name, 'Количество на складе': count})
        else:
            print('Введено некорректное количество.')

    def delivery_product(self, name, count):
        '''Выдача товара'''
        if isinstance(count, int):
            for i, dict in enumerate(self.product_list):
                if name in dict.values():
                    if self.product_list[i]['Количество на складе'] >= count:
                        self.product_list[i]['Количество на складе'] -= count
                        break
                    else:
                        print('На складе не такого количества товара.')
                        break
            else:
                print('Данный товар отсутствует на складе.')
        else:
            print('Введено некорректное количество.')


class OfficeEquipment:
    def __init__(self, name_model, weight):
        self.name_model = name_model
        self.weight = weight  # Вес


class Printer(OfficeEquipment):
    def __init__(self, name_model, weight, printing_speed, cartridge_resource):
        if isinstance(weight, (int, float)) and isinstance(printing_speed, int) and isinstance(cartridge_resource, int):
            super().__init__(name_model, weight)
            self.printing_speed = printing_speed
            self.cartridge_resource = cartridge_resource
        else:
            print('Данные введены некорректно.')
            self.name_model = ''
            self.weight = 0
            self.printing_speed = 0
            self.cartridge_resource = 0
            
    def __call__(self):
        return {'Наименование': self.name_model,
                'Вес': self.weight,
                'Скорость печати': self.printing_speed,
                'Ресурс картриджа': self.cartridge_resource}


class Scanner(OfficeEquipment):
    def __init__(self, name_model, weight, dpi):
        if isinstance(weight, (int, float)) and isinstance(dpi, int):
            super().__init__(name_model, weight)
            self.dpi = dpi
        else:
            print('Данные введены некорректно.')
            self.name_model = ''
            self.weight = 0
            self.dpi = 0

    def __call__(self):
        return {'Наименование': self.name_model,
                'Вес': self.weight,
                'Точек на дюйм': self.dpi}


class Xerox(OfficeEquipment):
    def __init__(self, name_model, weight, printing_speed, cartridge_resource, dpi):
        if isinstance(weight, (int, float)) and isinstance(printing_speed, int) and isinstance(cartridge_resource,
                                                                                               int) and isinstance(dpi,
                                                                                                                   int):
            super().__init__(name_model, weight)
            self.printing_speed = printing_speed
            self.cartridge_resource = cartridge_resource
            self.dpi = dpi
        else:
            print('Данные введены некорректно.')
            self.name_model = ''
            self.weight = 0
            self.printing_speed = 0
            self.cartridge_resource = 0
            self.dpi = 0

    def __call__(self):
        return {'Наименование': self.name_model,
                'Вес': self.weight,
                'Скорость печати': self.printing_speed,
                'Ресурс картриджа': self.cartridge_resource,
                'Точек на дюйм': self.dpi}


printer_1 = Printer('Samsung ML-1201', 5, 1600, 10000)
printer_2 = Printer('HP 500', 4, 1800, 8000)
scanner_1 = Scanner('Canon 1000', 1, 600)
xerox_1 = Xerox('HP Laser 135w', 4, 1650, 9000, 600)
xerox_1 = Xerox('HP Laser 135w', 4, 1650, 9000, 'qwe')

my_warehouse = Warehouse(printer_1(), 15)
my_warehouse.add_product(scanner_1(), 5)
my_warehouse.add_product(printer_2(), 10)
my_warehouse.add_product(printer_2(), '10')
print(my_warehouse.product_list)

my_warehouse.delivery_product(xerox_1(), 5)
my_warehouse.delivery_product(printer_1(), 5)
my_warehouse.delivery_product(printer_2(), 500)
print(my_warehouse.product_list)
