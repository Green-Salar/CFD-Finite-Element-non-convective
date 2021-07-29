import shapely
from shapely.geometry import LineString, Point
import numpy as np
import math
import math
import matplotlib.pyplot as plt
import numpy as np
from initial_variables import *


# Given these endpoints

# givven points of lines
def intersectionFinder(PoL1, PoL2):
    line1 = LineString([PoL1[0], PoL1[1]])
    line2 = LineString([PoL2[0], PoL2[1]])
    D = [line1, line2]
    int_pt = D[0].intersection(D[1])
    point_of_intersection = round(int_pt.x, 4), round(int_pt.y, 4)
    return point_of_intersection;


XYhorizontalCenter = []
XYverticalCenter = []
XYup = []
XYdown = []
XYleft = []
XYright = []
for x in np.arange(0.5, -0.51, -deltaXn):
    XYhorizontalCenter.append((round(x, 4), 0))

for y in np.arange(0.5, -0.51, -deltaYn):
    XYverticalCenter.append((0, round(y, 4)))

for teta in np.arange(0, pi + 0.001, delatTetaX):
    Xn = (math.cos(teta)) / 2
    Xn = (round(Xn, 4))
    XYup.append((Xn, 0.5))
    XYdown.append((Xn, -0.5))

for teta in np.arange(0, pi + 0.001, delatTetaY):
    Yn = (math.cos(teta)) / 2
    Yn = (round(Yn, 4))
    XYright.append((0.5, Yn))
    XYleft.append((-0.5, Yn))

points = []
# i shomarande bala be paiin az 0 shoroo mishe
# for baraye nime balaii
for i in range(0, int(Ny / 2)):

    # noghte avale khat az rast
    points.append(XYright[i])

    # j rast be chap az 0
    for j in range(1, Nx - 1):
        if j > 0 and j < (Nx / 2 - 1):
            # group of points bala
            GoP1 = [XYright[i], XYverticalCenter[i]]
            GoP2 = [XYup[j], XYhorizontalCenter[j]]
            point_of_intersection = intersectionFinder(GoP1, GoP2)
            points.append(point_of_intersection)
        #      print(point_of_intersection)

        if j == int(Nx / 2):
            # noghte vasat
            points.append(XYverticalCenter[i])

        if j > (int(Nx / 2)) and j < Nx - 1:
            GoP1 = [XYleft[i], XYverticalCenter[i]]
            GoP2 = [XYup[j], XYhorizontalCenter[j]]
            point_of_intersection = intersectionFinder(GoP1, GoP2)
            points.append(point_of_intersection)
    #        print(point_of_intersection)

    # noghte akhare khat
    points.append(XYleft[i])

# khatte vasat va paiin
for i in range(int(Ny / 2), Ny):

    # noghte avale khat az rast
    points.append(XYright[i])

    # j rast be chap az 0
    for j in range(1, Nx - 1):
        if j > 0 and j < (Nx / 2 - 1):
            # group of points bala
            GoP1 = [XYright[i], XYverticalCenter[i]]
            GoP2 = [XYdown[j], XYhorizontalCenter[j]]
            point_of_intersection = intersectionFinder(GoP1, GoP2)
            points.append(point_of_intersection)
        #     print(point_of_intersection)

        if j == int(Nx / 2):
            # noghte vasat
            points.append(XYverticalCenter[i])

        if j > (int(Nx / 2)) and j < Nx - 1:
            GoP1 = [XYleft[i], XYverticalCenter[i]]
            GoP2 = [XYdown[j], XYhorizontalCenter[j]]
            point_of_intersection = intersectionFinder(GoP1, GoP2)
            points.append(point_of_intersection)
    # print(point_of_intersection)

    # noghte akhare khat
    points.append(XYleft[i])

print('number of points', len(points))

xs = [x[0] for x in points]
ys = [x[1] for x in points]

squareNums = []
for i in range(0, Ny - 1):
    for j in range(0, Nx - 1):
        firstNum = i * Nx + j
        squareNums.append([firstNum, firstNum + 1, firstNum + Nx + 1, firstNum + Nx])

# print('number of points',len(squareNums))
# print(squareNums[0])

squaresQordinations = []
for i in range(0, len(squareNums)):
    square = []
    for j in squareNums[i]:
        square.append(points[j])
    squaresQordinations.append(square)

markazha = []
dsx = []
dsy = []
# ____ DSX DSY MARKAZ HA
for square in squaresQordinations:
    markaz = []
    Xvasate1 = (square[0][0] + square[1][0]) / 2
    Xvasate3 = (square[2][0] + square[3][0]) / 2
    Yvasate1 = (square[0][1] + square[1][1]) / 2
    Yvasate3 = (square[2][1] + square[3][1]) / 2
    vasate1 = (Xvasate1, Yvasate1)
    vasate3 = (Xvasate3, Yvasate3)
    GoP1 = [vasate1, vasate3]
    # print(GoP1)

    Xvasate2 = (square[1][0] + square[2][0]) / 2
    Xvasate4 = (square[3][0] + square[0][0]) / 2
    Yvasate2 = (square[1][1] + square[2][1]) / 2
    Yvasate4 = (square[3][1] + square[0][1]) / 2
    vasate2 = (Xvasate2, Yvasate2)
    vasate4 = (Xvasate4, Yvasate4)
    GoP2 = [vasate2, vasate4]
    # print(GoP2)
    markaz = intersectionFinder(GoP1, GoP2)
    markazha.append(markaz)

    dsx1 = (markaz[1] - Yvasate1)
    dsx2 = (markaz[1] - Yvasate2)
    dsx3 = (markaz[1] - Yvasate3)
    dsx4 = (markaz[1] - Yvasate4)
    temp = [dsx1, dsx2, dsx3, dsx4]
    dsx.append(temp)

    dsy1 = - (markaz[0] - Xvasate1)
    dsy2 = - (markaz[0] - Xvasate2)
    dsy3 = - (markaz[0] - Xvasate3)
    dsy4 = - (markaz[0] - Xvasate4)
    temp = [dsy1, dsy2, dsy3, dsy4]
    dsy.append(temp)

xs = [x[0] for x in points]
ys = [x[1] for x in points]

xd = [x[0] for x in markazha]
yd = [x[1] for x in markazha]
# plt.plot(XYleft,XYup,XYdown,XYright,XYhorizontalCenter,XYverticalCenter)
#plt.scatter(xd, yd, color='red')
#plt.scatter(xs, ys, color='green')
#plt.show()

