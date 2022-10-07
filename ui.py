import data_logger as  dl
from datetime import datetime as dt
from datetime import time
from encodings import utf_8

def hello():
    return print('Программа "калькулятор"\nПроизводит арифметические вычисления\n')


def input1():
    data = int(input('Введите первое число a = '))
    dl.input_value_logger(data)
    return data

def input2():
    data = int(input('Введите второе число b = '))
    dl.input_value_logger(data)
    return data

def result(data):
    dl.result_logger(data)
    return print('Результат операции = ', data)

def error(data):
    dl.error_logger(data)
    return print('Произошла ошибка ввода')

def action():
    deistvie = int(input('Выберете цифру соответствующую математической операции и нажмите "ввод"\n 1: "+"\n 2: "-"\n 3: "*"\n 4: "/"\n'))
    dl.action_logger(deistvie)
    return deistvie

