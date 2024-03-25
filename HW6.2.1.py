"""Задание 1

Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет

"""

#Создаём функцию с проверочным списком, по которому будем считать "повторки"
def yes_or_no(num_list):
    checking_array = []
    for num in num_list:
        checking_array.append(num)
        if checking_array.count(num) == 1:
            print("No")
        else:
            print("Yes")
    return "Programm finished."        

        
print(yes_or_no([1, 1, 1, 2, 3, 4, 2, 5, 5]))


"""Вывод
No
Yes
Yes
No
No
No
Yes
No
Yes
Programm finished.
"""
