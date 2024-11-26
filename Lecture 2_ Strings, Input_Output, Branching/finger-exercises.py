
# Number = 9 
# if Number > 0:
#   print("positive")
# elif Number == 0:
#   print("zero")
# else:
#   print("negative")

number = input("Please enter a number: ")

try:
    # First, try to convert the input to an integer
    intNumber = int(number)
    print(f"You entered an integer: {intNumber}")
except ValueError:
    try:
        # If it's not an integer, try to convert it to a float
        floatNumber = float(number)
        print(f"You entered a float: {floatNumber}")
    except ValueError:
        # If both conversions fail, the input is invalid
        print("Invalid input! Please enter a valid number.")