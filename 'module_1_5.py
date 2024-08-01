# immutable_val = tuple([[1, 3, 5,7], 4, 6, 'string', False])
# immutable_val_1 = 1, 3, 5, 7
# print(immutable_val)
# immutable_val [1] = 9 # - нельзя изменить элеиент кортежа
# print(immutable_val)
# immutable_val [0][1] = 4 # - но можно изменить элемент списка, входящего в кортеж
# print(immutable_val)
#immutable_val_3 = immutable_val + immutable_val_1 # - можно сложить кортежи между собой
# (конкатенация)
# immutable_val_3 = immutable_val * 4 # - можно продублировать содержание кортежа n-число раз
# при умножении на n
# print(immutable_val_3)


mutable_list = [2,4,6,8,'rock']
# print(mutable_list)
# mutable_list [1] = 19
# print(mutable_list)
# print(mutable_list[4])
# print(mutable_list [-1])
# print(mutable_list[0:4])
# mutable_list. append([1888, 5]) #- append - добавление элемента или нового списка
# в конец существующего списка
# print(mutable_list)
# mutable_list. extend('1888') # - extend - добавление строки в виде каждого знака,
# из которого она состоит
# mutable_list. extend([1,2,3]) # - также добавление списка в конец существующего
# mutable_list. remove(4)
# print(mutable_list)
print(6 in mutable_list) # - проверка наличия элемента в списке
print(6 not in mutable_list) # - проверка отсутствия элемента в списке
print(mutable_list[0:4]) # - работа со срезом: вывод элементов с 1 по 3
print(mutable_list[0:4:3]) # - работа со срезом: вывод элементов с 1 по 3 с шагом 3