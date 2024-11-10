a = 43
print(type(a))
a= "abc"
print(type(a))
x,y,z=34,45,67
print(x,y,z, sep=' | ', end=' | ')
print("hello")                  # 34 | 45 | 67 | hello

# to print int values with string
print("The value of x is = " + str(x))

#Other workaround to print string values  -- using f
print(f"String value of x = {x}, value of y = {y}")

first_name = input("Enter your First name")
print(type(first_name))
last_name = input("Enter your Last name")
print("Your first name is ", first_name, "and your last name is ", last_name)