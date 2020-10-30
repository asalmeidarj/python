"""1° derivada de uma função f em um ponto p por aproximação"""

from sympy import sympify

def recebe():
    expr = input('Derivada da função: ')
    ponto = input('ponto: ')
    return (sympify(expr), sympify(ponto))


f, p = recebe()  # A função f e o ponto p recebem os valores inseridos
deltx = 10**5
result = (f.subs('x', p + deltx) - f.subs('x', p - deltx))/(2*deltx)
print(result)
