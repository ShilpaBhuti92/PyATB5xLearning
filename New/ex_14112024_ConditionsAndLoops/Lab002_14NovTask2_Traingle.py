# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is

# equilateral (all sides are equal), or
# isosceles (exactly two sides are equal), or
# scalene (no sides are equal).

# Use an if-else statement to classify the triangle.

side1 = int(input("Enter the side1 of the triangle: "))
side2 = int(input("Enter the side2 of the triangle: "))
side3 = int(input("Enter the side3 of the triangle: "))

print(f"The sides of the triangle: {side1, side2, side3}")

if side1 == side2 and side2 == side3 :
    print("Equilateral")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("isosceles")
else:
    print("Scalene")
