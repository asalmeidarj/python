import numpy as np
import matplotlib.pyplot as plt

npontos = 100
pessoa1 = np.random.rand(npontos)*60
pessoa2 = np.random.rand(npontos)*60

xe = list()
ye = list()

xf = list()
yf = list()

ocorrencias = 0
for i in range(npontos):
    if (abs(pessoa1[i]-pessoa2[i]))<=10:
        xe.append(pessoa1[i])
        ye.append(pessoa2[i])
        ocorrencias += 1
    else:
        xf.append(pessoa1[i])
        yf.append(pessoa2[i])


plt.figure(figsize=(7,8))
#plt.scatter(pessoa1, pessoa2, s=1)
plt.scatter(xe, ye, s=10, edgecolors='orange')
plt.scatter(xf, yf, s=10, edgecolors='#4040ff')
plt.title(f'A probabilidade de encontro é aproximadamente {ocorrencias/npontos}')
plt.show()