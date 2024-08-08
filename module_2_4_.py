numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
len_ = len(numbers)
numbers.remove(1)
print(numbers)
primes = []
not_primes = []
#not_prime = False
for i in numbers:
    for j in numbers:
            if j <= i:
                if i % j > 0:
                    print(f'{i} / {j} = {i / j} - простое')
                    primes.append(i)
                    print(f' простые числа: {primes} ')
                    break

                if i % j == 0:
                    #print(f'{i} / {j} = {i/j} - составное')
                    not_primes.append(i)
                    print(f' составные числа: {not_primes}')
                    break
