# for i in range(3, 18, 2): # диапазон, где 3 - начальное значение, 18 - конечное, 2 - шаг
#     print(i)
# здесь значение переменной i будет меняться в диапазоне от 3 до 18 с шагом 2 (увеличиваясь каждый раз на 2)
#for i in 1, 1, 1, 1:
    #print(i)
# for i in 'carpetenebrum':
#     print(i)
# list_ = ['one', 'two', 'three']
# for i in list_:
#     print(i)
#  #   print(i, end= ',')
# list_ = ['one', 'two', 'three'] # задача пройтись по списку и убать перерменную three
# for i in list_:
#     if i == 'three':
#         list_.remove(i)
# print(list_)

# list_2 = [1, 2, 3, 4, 5, 1] # найдем сумму элементов списка
# можно так:
# sum_ = sum(list_2)
# print(sum_)
# будем искать через цикл for:
# sum_ = 0
# for i in range(len(list_2)):
#     sum_ += list_2[i] # эта запись равнозначна 0 + элемент списка с номером i
#     # sum_ = sum_ + list_2[i]
# print(sum_)

# for i in range(5): # функция range возвращает последовательность в диапазоне от нуля до указанного значения
                    # 0, 1, 2, 3, 4 -  последнее (5) не входит в последовательность
# for i in range(len(list_)): # последовательность от 0 до значения len, равного количеству элементов спbcка
#     list_[i] = 'число' # можно заменить элементы списка
# print(list_)

# Выведем таблицу умножения с помощью цикла for (например от 1 до 10)
 # функция range принимает три параметра: start, stop, step = начало последовательности, конец, шаг

# for i in range (1, 11): # берется первый элемент последовательности i = 1
#     for j in range (1, 11): # для первого элемента верхней последовательности перербираются элементы
#                             # данной последовательности: j = 1, j = 2, j = 3 и т.д.
#                             # После достижения j = 10, происходит возврат к верхнему циклу, i принимает значение 2 и т.д.
#         print(f'{i} × {j} = {i * j}')

#for со словарями
dict_ = {'a': 1, 'b': 2, 'c': 3, 'e': 4}
# print(dict_['a'])
# for i in dict_:
#     print(i, dict_[i]) # i принимает значение ключа в словаре
for i, k in dict_.items():
    print(i, k)