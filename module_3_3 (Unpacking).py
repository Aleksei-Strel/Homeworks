# Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра
# со значениями по умолчанию (например сейчас это: 1, 'строка', True).
def print_params(a = 1, b = 'nile', c = True):
    print(a, b, c) # Функция должна выводить эти параметры

# 1.Создайте список values_list с тремя элементами разных типов.
# 2. Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params,
# и значениями разных типов.
# 3. Передайте values_list и values_dict в функцию print_params, используя распаковку параметров
# (* для списка и ** для словаря).

values_list = ['mdb', False, 123]
values_dict = {'a': 'imago', 'b': False, 'c': 456}
print_params() # Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
print_params(2)
print_params(16, 'orf')
# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(b = 25, c = [1, 2, 3])

print_params(values_list)
print_params(*values_list)
print_params(values_dict)
print_params(**values_dict)

# Создайте список values_list_2 с двумя элементами разных типов
# Проверьте, работает ли print_params(*values_list_2, 42)

values_list_2 = [3.14, 'sear']
print_params(*values_list_2, 42)




# Параметры по умолчанию

# def test(a = 2, b = True):
#     print(a, b)
#test()
# При вызове функции параметры можно переназначить:
#test(a = False, b = 4)
#test([1, 2]) # можно вставить список. В данном случае он встал на место первого параметра
#test(*[1, 2]) # можно использовать *, тогда каждый элемент встанет на место соответсвующего параметра
                # для распаковки словаря использовать **

# def sum_of_values(a, b, c):
#     return a + b + c
# values = [1, 2, 3]
# result = sum_of_values(*values)
# print(result)


# В этом примере оператор * упаковывает оставшуюся часть списка my_list в переменную c.
# my_list = [1, 2, 3, 4]
# a, b, *c = my_list
# print(a, b, c)

# Оператор * можно использовать для распаковки итерируемого списка в новый список или кортеж:
# my_list = [1, 2, 3]
# new_list = [*my_list, 4, 5, 6]
# print(new_list)
# my_tuple = (1, 2, 3)
# new_tuple = (*my_tuple, 4, 5, 6)
# print(new_tuple)

# В этом примере оператор ** используется для распаковки словаря details
# и передачи его пар ключ-значение в качестве аргументов ключевых слов в функцию print_details.
# def print_details(name, age):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#
# details = {"name": "John", "age": 30}
# print_details(**details)

# В приведенном коде определяются два словаря dict1 и dict2. А оператор ** используется для
# распаковки их пар ключ-значение и объединения в один словарь combined_dict
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
#
# combined_dict = {**dict1, **dict2}
#
# print(combined_dict)


# Параметры *args и *kwargs могут использоваться в функции вместе с другими параметрами. Например:
# def sum(num1, num2, *nums):
#     result = num1 + num2
#     for n in nums:
#         result += n
#     return result
#
#
# print(sum(1, 2, 3))
# print(sum(1, 2, 3, 4))

sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
print(sales.items())


