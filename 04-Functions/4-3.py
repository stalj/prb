import math
def triangle_area(a,b,c):
    s=0.5*(a+b+c)
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area
first_area= triangle_area(3, 4, 5)
second_area= triangle_area(5, 12, 13)
third_area= triangle_area(7, 24, 25)

print(f'The area of ​​a triangle with sides 3, 4, 5 is {first_area}')
print(f'The area of ​​a triangle with sides 5, 12, 13 is {second_area}')
print(f'The area of ​​a triangle with sides 7, 24, 25 is {third_area}')