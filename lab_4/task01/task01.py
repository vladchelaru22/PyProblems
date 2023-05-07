import random as rd
import math

def random_points(radius, x_center, y_center):
    while True:
        x = rd.uniform(x_center - radius, x_center + radius)
        y = rd.uniform(y_center - radius, y_center + radius)
        if (x - x_center) ** 2 + (y - y_center) ** 2 < radius ** 2:
            return x, y