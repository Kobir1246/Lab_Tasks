def triangle_area(base, height):
    return 0.5 * base * height

base = int(input('Enter a base: '))
height = int(input('Enter a height: '))
area = triangle_area(base, height)
print(f"The area of the triangle is {area}")
