# Write a program that prints the sum of the prime
# numbers greater than 2 and less than 1000. Hint: you probably want
# to use a for loop that is a primality test nested inside a for loop that
# iterates over the odd integers between 3 and 999.

sum = 0
for i in range(3, 1000, 2):
    primality_flag = True 
    for j in range(3, i, 2):
        if i%j == 0:
            primality_flag = False 
            break 
    if primality_flag:
        sum = sum + i 
print(sum) 

# for j in range(3, 4, 2):
#     print(j)