print(99//5) # целочисленное деление
print(99/5) # деление
print(type(5))  # integer - целое число
print(99 % 5) # функция для нахождения целого числа остатка после деления
print(type(2.0))
print(type(True), type(False)) # boolean - только с заглавной

# 1st program Арифметика
print(9**0.5 * 5)

# 2nd program Сравнение or и and
print(9.99 > 9.98 and 1000 != 1000.1)
print(9.99 < 9.98 or 1000 == 1000.1)

# 3d program Сложная арифметика
a = '1234'
b = '5678'
print(int(a[1:3]) + int(b[1:3])) # изменение типа данных со строки (str) на число (int)


# 4th program Всё и сразу
a= 13.42
print(int(a)) # целая часть a
ai= int(a)
b= 42.13
bi= int(b) # целая часть b
print(a-ai)
print(b-bi)
a2= a-ai # дробная часть a
a3= a2*100 # дробная часть для сравнения
print(a3)
b2= b-bi # дробная часть b
b3=b2*100 # дробная часть для сравнения
print(ai==b3 or bi==a3)

a = 3.1415926
print (a)
r = round(a, 3) # округление до определенного знака
print(r)

# Переделано 4th program Всё и сразу
a= 13.42
print(int(a))
ai= int(a)
ai2=a-ai
ai2r=round(ai2,2)
print(ai2r)
b= 42.13
print(int(b))
bi= int(b)
bi2=b-bi
bi2r=round(bi2,2)
print(bi2r)
a3=ai2r*100
print(a3)
b3=bi2r*100
print(b3)
print(ai==b3 or bi==a3)