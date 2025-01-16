def find_quadrant(x, y):
    if x == 0 and y == 0:
        return "Point is at the origin (0,0)"
    elif x == 0:
        return "Point is on the Y-axis"
    elif y == 0:
        return "Point is on the X-axis"
    elif x > 0 and y > 0:
        return "Point is in the first quadrant"
    elif x < 0 and y > 0:
        return "Point is in the second quadrant"
    elif x < 0 and y < 0:
        return "Point is in the third quadrant"
    else:
        return "Point is in the fourth quadrant"

# Example input
x = 5
y = 2
print(f"Point P({x},{y}) is {find_quadrant(x, y)}")
