# Создаём функцию get_multiplied_digits и параметр number в ней
def get_multiplied_digits(number):
    # Создаём переменную str_number и записываем строковое представление(str) числа number в неё
    str_number = str(number)
    # Отделение первой цифры в числе: создание переменной first
    first = int(str_number[0])
    while str_number.endswith('0'):  # отсекаем нули в конце number
        str_number = str_number[0:len(str_number) - 1]
    if len(str_number) == 1:
        return int(str_number)
    elif len(str_number) > 1:
        # Возвращайте значение first
        return first * get_multiplied_digits(int(str_number[1:]))


# Вывод результата
result = get_multiplied_digits(4020300)
print(result)
