import os
from errors import *

def getterSig():
    if os.getlogin() == 'Jheremi.Villarreal':
        sign = 'JHV'
    elif os.getlogin() == 'David.Spenik':
        sign = 'DMS'
    elif os.getlogin() == 'Christian.Arroyo':
        sign = 'CMA'
    elif os.getlogin() == 'Rindy.Myers':
        sign = 'RMY'
    elif os.getlogin() == 'Zackary.Alcala':
        sign = 'ZJA'
    elif os.getlogin() == 'Jay.Compean':
        sign = 'JAC' 
    elif os.getlogin() == 'Julianne.Thompson':
        sign = 'JMT'
    elif os.getlogin() == 'Aaren.Perez':
        sign = 'AAP'
    elif os.getlogin() == 'Ricardo.Campos':
        sign = 'RCP'     
    else:
        warnpopupmsg("Please type in your signature since it is not in our system.")
        sign = '000'
        sign = signpopupmsg(sign)   
    return sign
