
# def my_sum(n, *args, txt = 'Sum of numbers'):
#     s = 0 # произвольная переменная, которая будет принимать значение аргумента
#     for arg in range(len(args)):
#         s += args[arg] ** n # += - для каждого последующего аргумента
#     print(txt + ':', s)
#
#
# my_sum(1, 2,3,4,5)

# Объявляем функцию
def single_root_words(root_word, *other_words):
# Создаём пустой список
    same_words = []
    root_word_lower = root_word.lower()
# Перебор подходящих слов
    for word in other_words:
        other_words_lower = word.lower()
        # Условие при котором добавляются слова в результирующий список same_words
        if root_word_lower in other_words_lower or other_words_lower in root_word_lower:
            same_words.append(word)
        # Возврат образованного функцией списка same_words
    return same_words
# Вызов функции single_root_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
# Вывод результата
print(result1)
print(result2)


