# Assume you are given a positive integer variable named N. Write a piece of Python code that finds the cube root of N. The code prints the cube root if N is a perfect cube or it prints error if N is not a perfect cube. Hint: use a loop that increments a counter—you decide when the counter should stop.

# work, but no break mechanism to stop
# N = 9
# flag_cube = False
# for i in range(N):
#     if i**3 == N:
#         flag_cube = True 
#         print(N, "is a perfect cube")
# if not flag_cube:
#     print("an error occured") 

# with break mechansim, but too verbose 
# N = 8
# flag_cube = False
# flag_counter = False 
# counter = 0
# for i in range(N):
#     while counter**3 >= N:
#         flag_counter = True
#         if counter**3 == i**3:
#             flag_cube = True
#             print(N, "is a perfect cube")
#         break 
#     counter += 1
#     if flag_counter:
#         break 
# if not flag_cube:
#     print("an error occured")
    
# suggested by ddb, use a single loop 
# N = 9
# counter = 0
# flag_cube = False 
# while counter**3 <= N:
#     if counter**3 == N:
#         print(N, "is a pefect cube")
#         flag_cube = True
#     counter += 1 
# if not flag_cube:
#     print("an error occured")

# course solution 
N = 8
i = 1
while i**3 < N:
    i += 1
if i**3 == N:
    print(i)
else:
    print("error")
# typical guess and check solution
# check the first integer that makes the i**3 < N condition false 
# to see if it can be the cube root 