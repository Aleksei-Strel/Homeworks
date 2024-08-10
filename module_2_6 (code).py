# def generate_password(n):               # (3, 4, 5, 6, 7, 8, 9 ... 17, 18, 19, 20), n = 17
#     password = []
#     for i in range(1, n):               # i = 1, 2, 3 ... 16
#         for j in range(i + 1, n + 1):   # j = 2, 3, 4 ... 17 - если i = 2,  j = 3, etc.
#             if n % (i + j) == 0:        # 17 / (1 + 2), (1+3) ... etc.
#                 twin = str(i) + str(j)
#                 password.append(twin)
#     return password
#
# for n in range(3, 21):
#     n = int(input('Введите число от 3 до 20: '))
#     password = generate_password(n)
#     print('Для числа', n, 'пароль будет:', *password)
#     break

def generate_password(n):
    password = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                password += str(i) + str(j)
    return password

n = int(input('Введите число от 3 до 20: '))
password = generate_password(n)
print(f'Для числа {n} пароль будет: {password}')
