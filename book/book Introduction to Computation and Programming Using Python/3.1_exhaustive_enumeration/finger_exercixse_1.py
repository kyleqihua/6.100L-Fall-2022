# Return the largest advisor 
x = int(input("enter an integer greater than 2: "))
smallest_divisor = None
largest_divisor = None
for guess in range(2, x):
    if x%guess == 0:
        smallest_divisor = guess 
        break
if smallest_divisor != None:
    largest_divisor = x//smallest_divisor
    print("largest divisor of", x, "is", largest_divisor)
else: 
    print(x, "is a prime number, so the largest divisor of it does not exit")