import math

import numpy
import numpy as np

pi = math.pi
Nx = 15
Ny = 15
W=1
H=1
delatTetaX = pi / (Nx - 1)
delatTetaY = pi / (Ny - 1)
deltaYn = W / (Ny - 1)
deltaXn = H / (Nx - 1)
k = 44  # W/m2C
ro = 7830  # kg/m3
cp = 481  # j/kgC
alpha = k / (ro * cp)
dt = 1
T = np.zeros(Nx * Ny)
for i in range(0, int(Nx * Ny)):
    T[i]=50
rightEdge = []
leftEdge = []

for i in range(1, Ny):
    rightEdge.append(i*Nx)
    leftEdge.append(i*Nx - 1)

leftEdge.append(Ny * Nx - 1)
top = []
bot = []
for i in range(0, Nx):
    top.append(i)
    bot.append((Nx * Ny) - Nx + i)

cornersPadSaatGard = [0, Nx - 1, Ny * Nx - 1, (Ny - 1) * Nx]

# <editor-fold desc="Description"
#
# for i in rightEdge:
#     T[i] = 115
# for i in leftEdge:
#     T[i] = 115
# for i in bot:
#     T[i] = 115
# for i in top:
#     T[i] = 535
#
# T[cornersPadSaatGard[0]] = (115 + 535) / 2
# T[cornersPadSaatGard[1]] = (115 + 535) / 2
#
# >

# </editor-fold>

edges115 = []
edges115 = np.concatenate((leftEdge,rightEdge,bot),axis=0)