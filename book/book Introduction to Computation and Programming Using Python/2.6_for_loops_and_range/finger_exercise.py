# my first version 
# sum = 0
# for i in range(3, 1000):
#     if i%2 != 0:
#         prime_flag = True 
#         for j in range(3, i, 2):
#             if i%j == 0:
#                 # i is not a prime number 
#                 prime_flag = False  
#         if prime_flag or i == 3: 
#             sum = sum + i 
# print(sum)

sum = 0
# sum = 2 # if include 2
for i in range(3, 1000, 2):
    prime_flag = True 
    for j in range(3, i, 2):
        if i%j == 0:
            prime_flag = False  
            break 
    if prime_flag: 
        sum = sum + i 
print(sum)