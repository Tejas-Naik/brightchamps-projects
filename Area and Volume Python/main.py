"""
Area and Volume Calculator in Python
-----------------------------------
This program demonstrates how to calculate area and volume of various shapes
using Python functions and basic math operations.

Designed for Grade 11 students learning Python basics.
"""

import math
import time

def print_header(title):
    """Prints a formatted header for better readability."""
    print("\n" + "=" * 50)
    print(f"{title.center(50)}")
    print("=" * 50)

def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): Length of the rectangle
        width (float): Width of the rectangle
        
    Returns:
        float: Area of the rectangle
    """
    return length * width

def calculate_circle_area(radius):
    """
    Calculate the area of a circle.
    
    Args:
        radius (float): Radius of the circle
        
    Returns:
        float: Area of the circle
    """
    return math.pi * radius ** 2

def calculate_triangle_area(base, height):
    """
    Calculate the area of a triangle.
    
    Args:
        base (float): Base of the triangle
        height (float): Height of the triangle
        
    Returns:
        float: Area of the triangle
    """
    return 0.5 * base * height

def calculate_cube_volume(side):
    """
    Calculate the volume of a cube.
    
    Args:
        side (float): Length of a side of the cube
        
    Returns:
        float: Volume of the cube
    """
    return side ** 3

def calculate_sphere_volume(radius):
    """
    Calculate the volume of a sphere.
    
    Args:
        radius (float): Radius of the sphere
        
    Returns:
        float: Volume of the sphere
    """
    return (4/3) * math.pi * radius ** 3

def calculate_cylinder_volume(radius, height):
    """
    Calculate the volume of a cylinder.
    
    Args:
        radius (float): Radius of the cylinder
        height (float): Height of the cylinder
        
    Returns:
        float: Volume of the cylinder
    """
    return math.pi * radius ** 2 * height

def get_valid_float_input(prompt):
    """
    Get a valid float input from the user.
    
    Args:
        prompt (str): Message to display to the user
        
    Returns:
        float: Valid float input from the user
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def area_calculator():
    """Interactive area calculator for different shapes."""
    print_header("AREA CALCULATOR")
    
    print("Choose a shape to calculate its area:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        print("\n--- Rectangle Area ---")
        length = get_valid_float_input("Enter length: ")
        width = get_valid_float_input("Enter width: ")
        area = calculate_rectangle_area(length, width)
        print(f"The area of the rectangle is {area:.2f} square units")
        
    elif choice == "2":
        print("\n--- Circle Area ---")
        radius = get_valid_float_input("Enter radius: ")
        area = calculate_circle_area(radius)
        print(f"The area of the circle is {area:.2f} square units")
        
    elif choice == "3":
        print("\n--- Triangle Area ---")
        base = get_valid_float_input("Enter base: ")
        height = get_valid_float_input("Enter height: ")
        area = calculate_triangle_area(base, height)
        print(f"The area of the triangle is {area:.2f} square units")
        
    else:
        print("Invalid choice. Please try again.")

def volume_calculator():
    """Interactive volume calculator for different 3D shapes."""
    print_header("VOLUME CALCULATOR")
    
    print("Choose a shape to calculate its volume:")
    print("1. Cube")
    print("2. Sphere")
    print("3. Cylinder")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        print("\n--- Cube Volume ---")
        side = get_valid_float_input("Enter side length: ")
        volume = calculate_cube_volume(side)
        print(f"The volume of the cube is {volume:.2f} cubic units")
        
    elif choice == "2":
        print("\n--- Sphere Volume ---")
        radius = get_valid_float_input("Enter radius: ")
        volume = calculate_sphere_volume(radius)
        print(f"The volume of the sphere is {volume:.2f} cubic units")
        
    elif choice == "3":
        print("\n--- Cylinder Volume ---")
        radius = get_valid_float_input("Enter radius: ")
        height = get_valid_float_input("Enter height: ")
        volume = calculate_cylinder_volume(radius, height)
        print(f"The volume of the cylinder is {volume:.2f} cubic units")
        
    else:
        print("Invalid choice. Please try again.")

def interactive_demo():
    """Run an interactive demo to calculate areas and volumes."""
    print_header("AREA AND VOLUME CALCULATOR")
    print("Welcome to the Area and Volume Calculator!")
    print("This program helps you calculate the area of 2D shapes")
    print("and the volume of 3D shapes.")
    
    while True:
        print("\nWhat would you like to calculate?")
        print("1. Area of a 2D shape")
        print("2. Volume of a 3D shape")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            area_calculator()
        elif choice == "2":
            volume_calculator()
        elif choice == "3":
            print("\nThank you for using the Area and Volume Calculator!")
            break
        else:
            print("Invalid choice. Please try again.")

def formula_guide():
    """Display formulas for area and volume calculations."""
    print_header("FORMULA GUIDE")
    
    print("--- 2D Shape Area Formulas ---")
    print("Rectangle: A = length × width")
    print("Circle: A = π × radius²")
    print("Triangle: A = ½ × base × height")
    
    print("\n--- 3D Shape Volume Formulas ---")
    print("Cube: V = side³")
    print("Sphere: V = (4/3) × π × radius³")
    print("Cylinder: V = π × radius² × height")

def main():
    """Main function to run the program."""
    print_header("PYTHON AREA AND VOLUME CALCULATOR")
    print("A learning tool for Grade 11 students")
    
    while True:
        print("\nMAIN MENU")
        print("1. Interactive Calculator")
        print("2. View Formulas")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            interactive_demo()
        elif choice == "2":
            formula_guide()
        elif choice == "3":
            print("\nThank you for learning about area and volume calculations!")
            print("Exiting program...")
            time.sleep(1)
            break
        else:
            print("Invalid choice. Please try again.")

# This is the entry point of the program
if __name__ == "__main__":
    main()
