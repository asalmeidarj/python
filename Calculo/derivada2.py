"""Derivada de ordem 2 de uma função f em um ponto p por aproximação"""

from sympy import sympify

def recebe():
    expr = input('2ª Derivada da função: ')
    ponto = input('ponto: ')
    return (sympify(expr), sympify(ponto))

def derivada2(func, p):
    deltx = 10**(-4)
    p1 = (func.subs('x', p + 2*deltx) - 2*func.subs('x', p + deltx) + func.subs('x', p))/(deltx**2)
    p2 = (func.subs('x', p - 2*deltx) - 2*func.subs('x', p - deltx) + func.subs('x', p))/(deltx**2)
    return (p1 + p2)/2


f, p = recebe()  # A função f e o ponto p recebem os valores inseridos
print (derivada2(f, p))