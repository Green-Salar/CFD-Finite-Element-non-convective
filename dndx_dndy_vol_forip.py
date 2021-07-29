import numpy as np
import math
import math
import matplotlib.pyplot as plt
import numpy as np
from dnds_dndt import *


def dndx_dndy_vol_ip(ip, X, Y):
    dyds = 0
    dxds = 0
    dxdt = 0
    dydt = 0

    for i in range(0, 4):
        dyds = dyds + dnds[ip][i] * Y[i]
        dydt = dydt + dndt[ip][i] * Y[i]
        dxds = dxds + dnds[ip][i] * X[i]
        dxdt = dxdt + dndt[ip][i] * X[i]

    J = dxds * dydt - dyds * dxdt

    ### for voulume of sub cv
    dydsVol = 0
    dxdsVol = 0
    dxdtVol = 0
    dydtVol = 0

    for i in range(0, 4):
        dydsVol = dydsVol + dndsVol[ip][i] * Y[i]
        dydtVol = dydtVol + dndtVol[ip][i] * Y[i]
        dxdsVol = dxdsVol + dndsVol[ip][i] * X[i]
        dxdtVol = dxdtVol + dndtVol[ip][i] * X[i]

    volume = abs(dxdsVol * dydtVol - dydsVol * dxdtVol)

    dndx = [0, 0, 0, 0]
    dndy = [0, 0, 0, 0]

    for i in range(0, 4):
        dndx[i] = 1 / J * (dydt * dnds[ip][i] - dyds * dndt[ip][i])
        dndy[i] = 1 / J * (-dxdt * dnds[ip][i] + dxds * dndt[ip][i])

    return dndx, dndy, volume
