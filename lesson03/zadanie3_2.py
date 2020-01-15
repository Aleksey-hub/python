# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user(city, email, name, lastname, year, phone_number):
    print(f'{name} {lastname} {year} {city} {email} {phone_number}')


user(name='Иван', lastname='Иванов', year='1900', city='Екатеринбург', email='ivanov@mail.ru', phone_number='899999999')
