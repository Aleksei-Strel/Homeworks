def test_function(x):
    def inner_function():
        print('Я в области видимости функции test_function')
    if int(len(x)) <= 3:
        print('Too short')
    else:
        inner_function()


    inner_function() # Функция срабатывает, но ничего не возвращает, т.к. она вложенная
# inner_function() # Выдает ошибку по той же причине


test_function('red') # Здесь всё работает. При этом inner_function(), если она вызвана, срабатывает при каждом цикле.
# test_function('two')
#test_function('redneck')
