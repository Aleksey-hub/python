# Продолжить работу над первым заданием. Разработать методы,
# отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

class Warehouse:
    def __init__(self, product_description, count):
        self.product_list = [{'Описание товара': product_description, 'Количество на складе': count}]

    def add_product(self, name, count):
        '''Добавление товара на склад'''
        for i, dict in enumerate(self.product_list):
            if name in dict.values():
                self.product_list[i]['Количество на складе'] += count
                break
        else:
            self.product_list.append({'Описание товара': name, 'Количество на складе': count})

    def delivery_product(self, name, count):
        '''Выдача товара'''
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


class OfficeEquipment:
    def __init__(self, name_model, weight):
        self.name_model = name_model
        self.weight = weight  # Вес


class Printer(OfficeEquipment):
    def __init__(self, name_model, weight, printing_speed, cartridge_resource):
        super().__init__(name_model, weight)
        self.printing_speed = printing_speed
        self.cartridge_resource = cartridge_resource

    def __call__(self):
        return {'Наименование': self.name_model,
                'Вес': self.weight,
                'Скорость печати': self.printing_speed,
                'Ресурс картриджа': self.cartridge_resource}


class Scanner(OfficeEquipment):
    def __init__(self, name_model, weight, dpi):
        super().__init__(name_model, weight)
        self.dpi = dpi

    def __call__(self):
        return {'Наименование': self.name_model,
                'Вес': self.weight,
                'Точек на дюйм': self.dpi}


class Xerox(OfficeEquipment):
    def __init__(self, name_model, weight, printing_speed, cartridge_resource, dpi):
        super().__init__(name_model, weight)
        self.printing_speed = printing_speed
        self.cartridge_resource = cartridge_resource
        self.dpi = dpi

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

my_warehouse = Warehouse(printer_1(), 15)
my_warehouse.add_product(scanner_1(), 5)
my_warehouse.add_product(printer_1(), 10)
print(my_warehouse.product_list)

my_warehouse.delivery_product(xerox_1(), 5)
my_warehouse.delivery_product(printer_1(), 5)
my_warehouse.delivery_product(printer_2(), 500)
print(my_warehouse.product_list)