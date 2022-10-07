
from datetime import datetime as dt
from datetime import time
from encodings import utf_8

def input_value_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a',  encoding='utf-8') as file:
        file.write('{};input_value;{}\n'
                    .format(time, data))

def result_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a',  encoding='utf-8') as file:
        file.write('{};result;{}\n'
                    .format(time, data))

def error_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a',  encoding='utf-8') as file:
        file.write('{};error;{}\n'
                    .format(time, data))


def action_logger(data):
    if data == 1:
        data  = '+'
    elif data == 2:
        data  = '-'
    elif data == 3:
        data  = '*'
    elif data == 4:
        data  = '/'
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a',  encoding='utf-8') as file:
        file.write('{};function; "{}"\n'
                    .format(time, data))


