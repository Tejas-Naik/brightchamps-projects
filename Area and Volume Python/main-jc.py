import math
r = int(input("enter the radius of the circle"))
# value of pie
pie = math.pi
 
# area of the circle
print(pie * r * r)

#Finding surface area and volume of a sphere
# function for volume of sphere
def volumesphere(r):
  return (4/3)*3.14*r*r*r

# function for surface of sphere
def surfaceareasphere(r):
  return 4*3.14*r*r


radius=int(input("Enter radius of sphere:"))
volume = volumesphere(radius)
surfacearea = surfaceareasphere(radius)


print(volume)
print(surfacearea)

#Finding surface area and volume of sphere,cube,cone and cylinder

import math

def sphere_surface_area(radius):
    return 4 * math.pi * radius ** 2

def sphere_volume(radius):
    return (4/3) * math.pi * radius ** 3

def cube_surface_area(side_length):
    return 6 * side_length ** 2

def cube_volume(side_length):
    return side_length ** 3

def cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height

def cone_surface_area(radius, height):
    slant_height = math.sqrt(radius ** 2 + height ** 2)
    return math.pi * radius * (radius + slant_height)

def cone_volume(radius, height):
    return (1/3) * math.pi * radius ** 2 * height


print("Select a 3D shape:")
print("1. Sphere")
print("2. Cube")
print("3. Cylinder")
print("4. Cone")

choice = int(input("Enter the number of the shape: "))

if choice == 1:
        radius = float(input("Enter the radius of the sphere: "))
        print("Surface area:", sphere_surface_area(radius))
        print("Volume:", sphere_volume(radius))

elif choice == 2:
        side_length = float(input("Enter the side length of the cube: "))
        print("Surface area:", cube_surface_area(side_length))
        print("Volume:", cube_volume(side_length))

elif choice == 3:
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))
        print("Surface area:", cylinder_surface_area(radius, height))
        print("Volume:", cylinder_volume(radius, height))

elif choice == 4:
        radius = float(input("Enter the radius of the cone: "))
        height = float(input("Enter the height of the cone: "))
        print("Surface area:", cone_surface_area(radius, height))
        print("Volume:", cone_volume(radius, height))

else:
        print("Invalid choice. Please select a valid option.")



#Finding Area of rectangle
def area():
  print('The area of the rectangle is ',length *breadth)
length=int(input("Please enter the value of length. "))
breadth=int(input("Please enter the value of breadth. ")) 
area()

#Finding Area of shapes
def area_triangle():
   base=int(input("Please enter the value of base. "))
   height=int(input("Please enter the value of height. "))
   triangle=(1/2*(base * height))
   print('The area of the triangle is {}'.format(triangle))
def area_rectangle():
    length=int(input('Please enter the value of length. '))
    breadth=int(input('Please enter the value of breadth. '))
    rectangle=(length * breadth)
    print('The area of the rectangle is {}.'.format(rectangle))
def area_square():
    side=int(input('Please enter thw sidse of the square. '))
    square=(side * side)
    print('The area of the square is {}.'.format(square))
def area_circle():
    radius=int(input('Please enter the radius of the circle. '))
    circle=(3.14 * radius* radius)
    print('The area of the circle is {}'.format(circle))
def area_semicircle():
    radii=int(input('Please enter the value of radius. '))
    semicircle=(1/2*(3.14 * radii))
    print('The area of the semicircle is {}.'.format(semicircle))
def area_parallelogram():
    base=int(input('Please enter the value of base. '))
    height=int(input('Please enter the value of height. '))
    parallelogram=(base * height)
    print('The area of the parallelogram is {}.'.format(parallelogram))
def area_rhombus():
    d1=int(input('Please enter the value of d1. '))
    d2=int(input('Please enter the value of d2. '))
    rhombus=1/2*(d1 * d2)
    print('The area of the rhombus is {}.'.format(rhombus))
def area_trapezium():
    height=int(input('Please enter the value of height. '))
    s1=int(input('Please enter the value of s1. '))
    s2=int(input('Please enter the value of s2. '))
    trapezium=height/2*(s1 + s2)
    print('The area of the trapezium is {}.'.format(trapezium))

print('Hello there, I can find area of any 2D figure.')
print('')
print("To find the area of triangle press 1")
print('To find the area of rectangle press 2')
print('To find the area of a square press 3')
print("To find the area of a circle press 4")
print('To find the area of the semicircle press 5')
print('To find the area of a parallelogram press 6')
print('To find the area of a rhombus press 7')
print('To find the area of a trapezium press 8')
print('')
a=input()
if a=='1':
  area_triangle()
elif a=='2':
  area_rectangle()
elif a=='3':
  area_square() 
elif a=='4':
  area_circle()  
elif a=='5':
    area_semicircle()
elif a=='6':
    area_parallelogram()
elif a=='7':
    area_rhombus()
elif a=='8':
    area_trapezium()
else:
    print("Invalid input")
    




