def cuboid_volume(a, b, c):
    return a * b * c

def cuboid_surface_area(a, b, c):
    return 2 * (a * b + b * c + a * c)

a = 3
b = 4
c = 5

volume = cuboid_volume(a, b, c)
surface_area = cuboid_surface_area(a, b, c)

print(f"Volume of the cuboid: {volume}")
print(f"Surface area of the cuboid: {surface_area}")
