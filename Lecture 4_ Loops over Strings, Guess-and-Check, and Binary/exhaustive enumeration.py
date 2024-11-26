# find the cube root of a perfect cube if it exists
# if the input is not a perfect cube, prints a message to that effect
# x = int(input("enter an integer: "))
# ans = 0
# while ans**3 < abs(x):
#     ans = ans + 1
# print(ans) 
# start from 0, enumberate all integers exhaustively until
# we target the number that makes ans**3 less than abs(x) False 
# that number is the one we need to check 
# if ans**3 != abs(x):
#     print(x, "is not a perfect cube")
# else: 
#     if x < 0:
#         ans = -ans
#     print("cube root of", x, "is", ans)


# maxVal = int(input("enter a postive integer: "))
# i = 0
# while i < maxVal:
#     i = i+1
# print(i) 

# test if an int > 2 is prime. if not, print smallest advisor 
# x = int(input("enter an integer greater than 2: "))
# smallest_divisor = None
# for guess in range(2, x):
#     if x%guess == 0:
#         smallest_divisor = guess 
#         break
# if smallest_divisor != None:
#     print("smallest divisor of", x, "is", smallest_divisor)
# else: 
#     print(x, "is a prime number")

# Return the largest advisor 
# x = int(input("enter an integer greater than 2: "))
# smallest_divisor = None
# largest_divisor = None
# for guess in range(2, x):
#     if x%guess == 0:
#         smallest_divisor = guess 
#         break
# if smallest_divisor != None:
#     largest_divisor = x//smallest_divisor
#     print("largest divisor of", x, "is", largest_divisor)
# else: 
#     print(x, "is a prime number, so the largest divisor of it does not exit")

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

# test if the pair of root and pwr exists. if not, print a message to that effect
# it is so hard to formalize my thoughts 
num = int(input("enter an integer to test the existence of the pair: "))
root = 2
pwr = 2 
pair_flag = False
for pwr in range(2, 6):
    if pow(root, 2) > num:
        break 
    root = root + 1
for pwr in range(2, 6):
    if pow(root, pwr) == num:
        print("the pair exists. the root is", root, "and the pwr is", pwr)
        pair_flag = True
        break 
    if pow(root, pwr) > num:
        break 
root = root + 1
if pow(root, 2) > num:
    break 
if pair_flag == False:
    print("the pair does not exist")
# while pow(root, pwr) <= num:

# for pwr in range(2, 6):
#     while pow(root, pwr) <= num:
#         if pow(root, pwr) == num:
#             print("the pair exists. the root is", root, "and the pwr is", pwr)
#             pair_flag = True
#             break 
#         root = root + 1



