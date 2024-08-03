my_dict = {'Samara': 63, 'Perm': 59, 'Orenburg': 56}
# my_dict2 = {'a': 123, 'b': 345}
# k = my_dict.pop('Perm')
# my_dict2 ['Perm'] = k
# print(my_dict2)
print(my_dict)
print(my_dict['Samara'])
print(my_dict.get('Sarstov')) #- метод .get - возвращает значение по указанному ключу,
# # в случае отсутствия верне none или указанную строку, пример ниже:
# print(my_dict.get('Saratov', 'Такого города нет'))
my_dict.update ({'Saratov': 64, 'Komi': 11})
print(my_dict)
print(my_dict.pop('Saratov')) #- метод .pop - удаляет ключ и возвращает соответствующее ему
# значение, можно сделать значением переменной,
# при выводе которой будет возвращено значение, которое соответствовало ключу
print(my_dict)

my_set = {1, 2, 5, 6, 7, 1, 7, 7, 5, 'bus', (3,5,7,9)}
print(my_set, type (my_set))
my_set.update([12, 44, 99]) # - метод .update - возможность добавить несколько элементов
print(my_set)
my_set.remove(7)
print(my_set)

