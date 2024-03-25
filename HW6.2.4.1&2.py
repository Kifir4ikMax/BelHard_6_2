"""Задание 4

С помощью декораторов реализовать конвейер сборки бургера

"""


#Создаём декоратор для "Булочек"
def bread_decorator(func):
    def wrapper():
        print("</------------\\>")
        result = func()
        print(f"<\\____________/>\n\n")
        return result
    return wrapper


#Создаём декоратор для "Помидор"    
def tomato_decorator(func):
    def wrapper():
        print("*** помидоры ****")
        result = func()
        return result
    return wrapper
    

#Создаём декоратор для "Салата"
def salad_decorator(func):
    def wrapper():
        print("~~~~ салат ~~~~~")
        result = func()
        return result
    return wrapper  
    

#Создаём декоратор для "Сыра"
def cheese_decorator(func):
    def wrapper():
        print("^^^^^ сыр ^^^^^^")
        result = func()
        return result
    return wrapper  
    
#Создаём декоратор для "Лука"
def onion_decorator(func):
    def wrapper():
        print("----- лук ------")
        result = func()
        return result
    return wrapper


#Оборачиваем основные функции "говядина" и "курица" в необходимые декораторы
@bread_decorator
@onion_decorator
@tomato_decorator
def beef():
    print("### говядина ###")
    
    
@bread_decorator
@cheese_decorator
@salad_decorator
def chicken():
    print("|||| курица |||| ")
   

#Вызываем основные функции
beef()
chicken()


"""Вывод

</------------\>
----- лук ------
*** помидоры ****
### говядина ###
<\____________/>


</------------\>
^^^^^ сыр ^^^^^^
~~~~ салат ~~~~~
|||| курица |||| 
<\____________/>

"""
