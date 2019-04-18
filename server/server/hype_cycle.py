import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

X = None
Y = None
POINT_NUM = 1000

# curve fitting by point tracing method
# the graph is inverted
def load_hype_cycle():
    global X, Y
    X = [0]
    Y = [0]
    img = Image.open('hype_cycle.bmp')
    n, m = img.size
    for i in range(0, n):
        y = []
        for j in range(0, m):
            rgb = img.getpixel((i, j))
            if rgb[0]+rgb[1]+rgb[2] < 255*3:
                y.append(j)
        X.append((i+1) / n)
        Y.append(1.0 - (np.mean(y)+1) / m)

# calc the y value of Hype Cycle at position x
def hype_cycle_value(x):
    if not X:
        load_hype_cycle()
    for i in range(0, len(X)-1):
        if X[i] <= x and X[i+1] > x:
            return Y[i] + (x - X[i]) / (X[i+1] - X[i]) * (Y[i+1] - Y[i])
    return 0.0

# draw the Hype Cycle by using matplotlib library
def show_hype_cycle(xx=None, yy=None):
    if not X:
        load_hype_cycle()
    plt.plot(X, Y)
    if xx and yy:
        plt.plot(xx, yy)
    plt.show()

# a naive way to calc the similarity of two discrete time series
def calc_loss(curve1, curve2):
    c1 = np.array(curve1)
    c2 = np.array(curve2)
    v1 = np.max(c1)
    v2 = np.max(c2)
    if v1 <= 0 or v2 <= 0:
        return 1e16
    loss = np.sum(np.abs(c1 / v1 - c2 / v2))
    return loss

# Mapping keywords to a point on Hype Cycle based on time series
# Return the relative position in input picture and the minimum loss
def get_pos(curve):
    n = len(curve)
    min_loss = 1e16
    pos = 0
    for i in range(1, POINT_NUM):
        xx = []
        yy = []
        for j in range(1, n+1):
            x = j / n * i / POINT_NUM
            xx.append(x)
            yy.append(hype_cycle_value(x))
        loss = calc_loss(curve, yy)
        if loss < min_loss:
            min_loss = loss
            pos = i / POINT_NUM
    return (pos, hype_cycle_value(pos)), min_loss

if __name__ == '__main__':
    # show_hype_cycle()
    print(get_pos([0, 1, 2, 3, 4, 5, 6, 7, 8]))
    print(get_pos([10, 9, 8, 2, 1, 0, 10, 2]))
    print(get_pos([0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 2.5]))