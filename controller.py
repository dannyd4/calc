import ui 
import real_number as rn
from datetime import datetime as dt
from time import time
import controller as c

def button_click():
    ui.hello()
    a = ui.input1()
    b = ui.input2()
    deistvie = ui.action()


    if deistvie == 1:
        ui.result(rn.plus(a, b))
    elif deistvie == 2:
        ui.result(rn.minus(a, b))
    elif deistvie == 3:
        ui.result(rn.mult(a, b))
    elif deistvie == 4:
        ui.result(rn.divide(a, b))
    else: ui.error()
    
exit
