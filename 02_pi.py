import numpy as np
import matplotlib.pyplot as plt

npontos_circulo = 0
npontos = 500000

x = np.random.rand(npontos)
y = np.random.rand(npontos)
dis_x = (0.5 - x) ** 2
dis_y = (0.5 - y) ** 2
dis_c = (dis_x + dis_y)**(1/2)

qx = list()
qy = list()
cx = list()
cy = list()
for i in range(npontos):
    if dis_c[i] < 0.5:
        npontos_circulo += 1
        cx.append(x[i])
        cy.append(y[i])
    else:
        qx.append(x[i])
        qy.append(y[i])

plt.figure(figsize=(7, 8))
plt.scatter(cx, cy, s=0.8)
plt.scatter(qx, qy, s=0.8)
uni = '\u03A0'
plt.title(f'O valor aproximado para {uni} -> {4*npontos_circulo/npontos}')
plt.show()

