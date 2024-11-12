# Problem to find the max between two ( 3,4) → 4

a, b = 3, 4

# Using Ternary operator
print(f"{a} is greater" if (a > b) else f"{b} is greater")

# Using If-else
if a > b:
    print(f"{a} is greater")
else:
    print(f"{b} is greater")
