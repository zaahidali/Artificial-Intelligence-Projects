import math as take, itertools as running
from collections import defaultdict as dictionary
from random import uniform as same
import matplotlib.pyplot as draw

def DisplayAndShowThePlot():
        clusters = 5
        plotGraph = draw.figure()
        out = list()
        data = MainProgram(SetData, clusters)
        for i, j in zip(SetData, data):
            out.append((i, j))
        result = sorted(out, key=lambda x: x[1])
        listOfValues = [list(v) for k, v in running.groupby(result, lambda x: x[1])]
        a0,a1 = 0,1
        for i, color in zip(listOfValues, colors):
            x = CalculateXYaxisValues(i)[a0]
            y = CalculateXYaxisValues(i)[a1]
            draw.scatter(x, y,  color=color,marker="*", s=50)
        draw.title('For K = ' + "5")
        plotGraph.savefig("plot.pdf", bbox_inches='tight')

green = 'green'
red = 'red'
blue = 'blue'
brown = 'brown'
pink = 'pink'
colors = [green, red, pink, blue, brown]

SetData = list()
def ReadDataFromFile():
    f1 = 1
    comma = ','
    filesData = open('data.txt', 'r')
    lines = filesData.read().splitlines()
    for element in lines[f1:]:
        item = [int(i.strip()) for i in element.split(comma)]
        SetData.append(item)
ReadDataFromFile()

def CalculateXYaxisValues(SetData):
    x_axis,y_axis = list(), list()
    a0,a1 = 0,1
    for i in SetData:
        x_axis.append(i[a0][a0])
        y_axis.append(i[a0][a1])
    return [x_axis, y_axis]

ForMinValues = 'min_%d'
ForMaxValues = 'max_%d'
def setCentroids(data_set, k):
    cpoint = list()
    v0 = 0
    axis = len(data_set[v0])
    XYminmaxValues = dictionary(int)
    for point in data_set:
        for i in range(axis):
            val = point[i]
            ForMinV = ForMinValues % i
            ForMaxV = ForMaxValues % i
            if val > XYminmaxValues[ForMaxV] or ForMaxV not in XYminmaxValues:
                XYminmaxValues[ForMaxV] = val
            elif val < XYminmaxValues[ForMinV] or ForMinV not in XYminmaxValues :
                XYminmaxValues[ForMinV] = val
            else:
                "Do nothing"
    for i in range(k):
        xymeans = list()
        for j in range(axis):
            min_val = XYminmaxValues[ForMinValues % j]
            max_val = XYminmaxValues[ForMaxValues % j]
            xymeans.append(same(min_val, max_val))
        cpoint.append(xymeans)
    return cpoint

def Meanmeans(means):
    dimension_number = len(means[0])
    center = list()
    for dimension in range(dimension_number):
        total = 0
        for point in means:
            total = total + point[dimension]
        center.append(total / float(len(means)))
    return center

def update(data_set, data_setting):
    new_means = dictionary(list)
    centroids_P = list()
    for res, point in zip(data_setting, data_set):
        new_means[res].append(point)
    for means in new_means.values():
        centroids_P.append(Meanmeans(means))
    return centroids_P

def calculate_distance(x2,x1):
    res = 0
    for values in range(len(x2) - 1):
        res = res+  pow((x2[values] - x1[values]), 2)
    return take.sqrt(res)

def XYmeans(data_means, cpoint):
    measure = list()
    for point in data_means:
        s = take.inf
        first = 0
        for i in range(len(cpoint)):
            val = calculate_distance(point, cpoint[i])
            if val < s:
                s = val
                first = i
        measure.append(first)
    return measure

def MainProgram(SetData, k):
    old_Values = None
    cpoint = setCentroids(SetData, k)
    Values = XYmeans(SetData, cpoint)
    final_cpoint = list()
    while Values != old_Values:
        new_cpoint = update(SetData, Values)
        final_cpoint = new_cpoint
        old_Values = Values
        Values = XYmeans(SetData, new_cpoint)
    for i, color in zip(final_cpoint, colors):
        draw.scatter(i[0], i[1], s=100)
    return Values

DisplayAndShowThePlot()
