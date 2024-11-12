# Write a program to take a user age and let him know if he can go the club.  21

age = int(input("Enter your age:\n"))

#Using ternary operator
print("You can go to the club" if (age >= 21) else "You can not go to club")

# Using If-else
if age >= 21:
    print("You can go to the club")
else:
    print("You can not go to club")