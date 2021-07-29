# grid and ds dx has been generated in th Grid file
# dnds dndt for integration points
import numpy as np
import math
import math
import matplotlib.pyplot as plt
import numpy as np
from Grid_and_ds_generator import *

dnds = []
dndt = []


def dnds_ip(t):
    dn1ds = (1 + t) / 4
    dn2ds = -(1 + t) / 4
    dn3ds = -(1 - t) / 4
    dn4ds = (1 - t) / 4
    dndss = [dn1ds, dn2ds, dn3ds, dn4ds]
    return dndss


def dndt_ip(s):
    dn1dt = (1 + s) / 4
    dn2dt = (1 - s) / 4
    dn3dt = -(1 - s) / 4
    dn4dt = -(1 + s) / 4
    dndtt = [dn1dt, dn2dt, dn3dt, dn4dt]
    return dndtt


ip_s = [0, -.5, 0, .5]
ip_t = [.5, 0, -.5, 0]
for ip in range(0, 4):
    s = ip_s[ip]
    t = ip_t[ip]
    dnds.append(dnds_ip(t))
    dndt.append(dndt_ip(s))

#   dnds dndt of volumes center of sub cv
ipVol_s = [0.5, -.5, -0.5, .5]
ipVol_t = [.5, 0.5, -.5, -0.5]
dndsVol = np.zeros((4, 4))
dndtVol = np.zeros((4, 4))
for i in range(0, 4):
    s = ipVol_s[i]
    t = ipVol_t[i]
    dndsVol[i] = dnds_ip(t)
    dndtVol[i] = dndt_ip(s)
