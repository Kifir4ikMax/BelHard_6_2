"""Задание 3

Написать функцию hello, которая принимает аргумент name - строку с именем и
выводит принтом "Привет, {name}"
Написать декоратор log_decorator, который перед выполнением
функции печатает на экран строку, вида
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}".
После выполнения функции напечатать строку "Выполнено {func.__name__}

"""


#Создаём декоратор с "обёрткой"
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Execute {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Executed {func.__name__}.")
        return result
    return wrapper    
        

#Оборачиваем основную функцию hello
@log_decorator
def hello(name, *args, **kwargs):
    print(f"Hello, {name}!")
hello("Max", "Kifir", age=31, weight=72)


"""Вывод

Execute hello with args: ('Max', 'Kifir') and kwargs: {'age': 31, 'weight': 72}
Hello, Max!
Executed hello.

"""
