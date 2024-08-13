# Создать переменную calls = 0 вне функций.
# Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
# Создать функцию string_info с параметром string и реализовать логику работы по описанию.
# Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
# Вывести значение переменной calls на экран(в консоль).


calls = 0


def count_calls(): # Функция count_calls подсчитывающая вызовы остальных функций.
    global calls
    calls += 1


def string_info(string):
    result = (len(string), string.upper(), string.lower()) # Функция string_info принимает аргумент -
    # строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
    count_calls()
    return result


def is_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string: #Функция is_contains принимает два аргумента:
            # строку и список, и возвращает True, если строка находится в этом списке,
            # False - если отсутствует. Регистром строки при проверке пренебречь
            result = True
            break
        else:
            result = False
            continue
    return result

# N.B.
# Преобразовать список строк в нижний или верхний регистр можно одним выражением:
# lowercase_list = [s.lower() for s in my_list]
# uppercase_list = [s.upper() for s in my_list] - my_lyst - преобразуемый список

print(string_info('рokoko'))
print(string_info('барокко'))
print(is_contains('ампир', ['модерн', 'готика', ]))
print(is_contains('аКМеизм', ['символизм', 'футуризм', 'акмеизм']))
print(calls)