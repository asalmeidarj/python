import numpy as np
import matplotlib.pyplot as plt

def func(x):
    """Retorna o módulo do seno de um valor dado."""
    return abs(np.sin(x))

npontos = 500000
x = np.random.rand(npontos)*2*np.pi
y = np.random.rand(npontos)

xg = list()  # Coordenada x do ponto abaixo do gráfico
yg = list()  # Coordenada y do ponto abaixo do gráfico

xe = list()  # Coordenada x do ponto acima do gráfico
ye = list()  # Coordenada y do ponto acima do gráfico

area_retangulo = 2*np.pi

"""Determinar os pontos abaixo e acima do gráfico"""
ocorrencias = 0
for i in range(npontos):
    if y[i] < func(x[i]):
        xg.append(x[i])
        yg.append(y[i])
        ocorrencias += 1
    else:
        xe.append(x[i])
        ye.append(y[i])

"""Plotar o gráfico"""
plt.figure(figsize=(7,8))
plt.scatter(xg, yg, s=0.8)
plt.scatter(xe, ye, s=0.8)
plt.title(f'A integral no intervalo [0, 2pi] de seno é {ocorrencias/npontos*area_retangulo}')
plt.show()



