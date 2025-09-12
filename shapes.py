import math

# Function to calculate area of rectangle
def rectangle_area(length, width):
    return length * width

# Function to calculate area of square
def square_area(side):
    return side ** 2

# Function to calculate area of circle
def circle_area(radius):
    return math.pi * (radius ** 2)

# Function to calculate area of triangle
def triangle_area(base, height):
    return 0.5 * base * height

def main():
    while True:
        print("\nMenu:")
        print("1. Calculate Rectangle Area")
        print("2. Calculate Square Area")
        print("3. Calculate Circle Area")
        print("4. Calculate Triangle Area")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            length = float(input("Enter rectangle length: "))
            width = float(input("Enter rectangle width: "))
            print(f"Rectangle Area: {rectangle_area(length, width)}")
        elif choice == "2":
            side = float(input("Enter square side: "))
            print(f"Square Area: {square_area(side)}")
        elif choice == "3":
            radius = float(input("Enter circle radius: "))
            print(f"Circle Area: {circle_area(radius)}")
        elif choice == "4":
            base = float(input("Enter triangle base: "))
            height = float(input("Enter triangle height: "))
            print(f"Triangle Area: {triangle_area(base, height)}")
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()