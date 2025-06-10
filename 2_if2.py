"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
first_string = input('Введите первую строку: ')
second_string = input('Введите вторую строку: ')
def strings(first_string, second_string):
    if first_string is str and second_string is str: #как проверить на принадлежность к строкам, чтобы было, что, если не принадлежит, то ноль 
        return(first_string, second_string)
    elif first_string == second_string:
        return ('1')
    elif len(first_string) > len(second_string):
        return('2')
    elif len(first_string) != len(second_string) and second_string == 'learn':
        return('3')
    else:
        return('0')
result = strings(first_string, second_string)
print(result)