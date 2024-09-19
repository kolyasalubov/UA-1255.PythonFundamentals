import math

def rectangle_area(height, width):
    return height * width

def triangle_area(base, height):
    return int(0.5*(base * height))

def circle_area(radius):
    return round(math.pi * math.pow(radius, 2), 2)


