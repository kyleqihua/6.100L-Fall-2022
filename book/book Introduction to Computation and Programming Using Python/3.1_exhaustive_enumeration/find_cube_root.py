# find the cube root of a perfect cube if it exists
# if the input is not a perfect cube, prints a message to that effect
x = int(input("enter an integer: "))
ans = 0
while ans**3 < abs(x):
    ans = ans + 1
print(ans) 
# start from 0, enumberate all integers exhaustively until
# we target the number that makes ans**3 less than abs(x) False 
# then we need to check that number 
if ans**3 != abs(x):
    print(x, "is not a perfect cube")
else: 
    if x < 0:
        ans = -ans
    print("cube root of", x, "is", ans)