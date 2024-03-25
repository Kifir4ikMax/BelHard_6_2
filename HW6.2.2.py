"""Задание 2

Написать функцию count_char, которая принимает строковое значение
STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
'буква': количество-вхождений-в-строку
}
например: {
'p': 2,
'y': 1,
}
STR_VAL = 'python is the fastest-growing major programming language'
Нельзя пользоваться collections.Counter!

"""

#Создаём функцию на подсчет ТОЛЬКО букв в строке
def count_char(str_val):
    letter_count = {}
    for i in str_val:
        if i.isalpha():
            letter_count[i] = str_val.count(i)
    return letter_count
print(count_char("python is the fastest-growing major programming language"))

"""Вывод

{'p': 2, 'y': 1, 't': 4, 'h': 2, 'o': 4, 'n': 4, 'i': 3, 's': 3, 'e': 3, 'f': 1, 'a': 5, 'g': 6, 'r': 4, 'w': 1, 'm': 3, 'j': 1, 'l': 1, 'u': 1}

"""
