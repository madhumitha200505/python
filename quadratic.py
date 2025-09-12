import math

def find_roots(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check if the discriminant is positive, negative or zero
    if discriminant > 0:
        # Two distinct real roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        # One real root
        root = -b / (2*a)
        return root
    else:
        # No real roots (complex roots)
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        root1 = f"{real_part} + {imaginary_part}i"
        root2 = f"{real_part} - {imaginary_part}i"
        return root1, root2

# Test the function
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

roots = find_roots(a, b, c)

if isinstance(roots, tuple):
    print(f"The roots are {roots[0]} and {roots[1]}")
else:
    print(f"The root is {roots}")