"""1° derivada de uma função f em um ponto p por aproximação"""

import numpy as np
from sympy import *

def ndeltx(num):
    return 10**(-num)

def recebe():
    expr = input('Derivada da função: ')
    ponto = input('no ponto: ')
    return (sympify(expr), sympify(ponto))

f, p = recebe()  # A função f e o pontos p recebem os valores inseridos
deltx = ndeltx(5)
result = (f.subs('x', p + deltx) - f.subs('x', p - deltx))/(2*deltx)
print(result)
