import numpy as np
import matplotlib.pyplot as plt
import math


def getGraphPoints(coordinates, vp, iDss):
    # iD = iDss * (1 - vGS/vp)
    vGS = 0.0
    while vGS >= -vp:
        iD = iDss * math.pow((1 + vGS/vp), 2)
        pt = [vGS, iD]
        coordinates.append(pt)
        vGS = vGS - 0.5


def plotGraph(coordinates):
    x_axis = []
    y_axis = []
    for item in coordinates:
        x_axis.append(item[0])
    for item in coordinates:
        y_axis.append(item[1])
    x = np.array(x_axis)
    y = np.array(y_axis)
    plt.title("Transconductance Curve")
    plt.xlabel("VGS")
    plt.ylabel("ID")
    plt.plot(x, y)
    plt.show()


def main():
    vp = float(input("Enter the pinchoff voltage value for the jfet(already in volts): "))
    iDss = float(input("Enter the IDSS value for the jfet(already in mA): "))
    #list of pair lists to graph
    graphCoordinates = []
    getGraphPoints(graphCoordinates, vp, iDss)
    print("Graph Coordinates:")
    print(graphCoordinates)
    plotGraph(graphCoordinates)


main()