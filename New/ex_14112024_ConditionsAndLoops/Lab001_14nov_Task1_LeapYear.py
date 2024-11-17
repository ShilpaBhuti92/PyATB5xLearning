# Checking for a Leap Year , 2024 → Yes

# Leap day occurs in each year that is a
# multiple of 4,
# except for years evenly divisible by 100 but not by 400.

year = int(input("Enter the year: "))

if year <= 1582:
    print("The year has to be greater than 1582, "
          "the first year the Gregorean calendar was employed.")
elif ((year % 4 == 0) and not (year % 100 == 0)) or (year % 400 == 0):
    print("it is a leap year")
else:
    print("NOT a leap year")
