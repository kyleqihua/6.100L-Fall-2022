# test if an int > 2 is prime. if not, print smallest advisor 
x = int(input("enter an integer greater than 2: "))
smallest_divisor = None
for guess in range(2, x):
    if x%guess == 0:
        smallest_divisor = guess 
        break
if smallest_divisor != None:
    print("smallest divisor of", x, "is", smallest_divisor)
else: 
    print(x, "is a prime number")


# test if an int > 2 is prime. if not, print smallest advisor 
# improve the code to make it faster 
# x = int(input("enter an integer greater than 2: "))
# smallest_divisor = None
# if x%2 == 0:
#     smallest_divisor = 2
# else:
#     for guess in range(3, x, 2):
#         if x%guess == 0:
#             smallest_divisor = guess 
#             break
# if smallest_divisor != None:
#     print("smallest divisor of", x, "is", smallest_divisor)
# else: 
#     print(x, "is a prime number")