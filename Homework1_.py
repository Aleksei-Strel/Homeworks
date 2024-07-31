#Базовые структуры (второй вариант)
a = 'риформинг'
print(a)
lengh_a = len(a) # считает кол-во знаков в строке
print('Кол-во знаков: '+str(lengh_a))
first = 25
second = 15
summa = int(first) + int(second)
print(summa)
diff = int(first) - int(second)
print(diff)
third = 5
#Расчет среднего арифмитического:
#Пример:
numbers = [4, 8, 6, 5, 3, 2] #Список
average = sum(numbers) / len(numbers) #Функция sum() возвращает сумму всех элементов списка, а функция len() возвращает количество элементов в списке.
print(average)

#Решение:
numbers = [int(first),int(second),int(third)]
mean = sum(numbers) / len(numbers)
print(mean)

a = '5'
b = '10'
c = '15'
f = int(a)*int(b)+int(a)*int(c)
print(f)
d = int(f)**3
print(d)
f = int(d)/2
print(f)