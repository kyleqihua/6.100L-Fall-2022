# count = 0
# odd_flag = False 
# largest_odd = 1
# while count < 10:
#     num = int(input("please enter an integer: "))
#     if num%2 == 1:
#         odd_flag = True 
#         if largest_odd <= num:
#             largest_odd = num
#     count = count + 1
# if odd_flag == False:
#     print("no odd number was entered")
# else:
#     print("the largest odd number is", largest_odd)

# with the help from ddb 
count = 0
odd_flag = False 
largest_odd = None 
while count < 10:
    num = int(input("please enter an integer now (after ten times of input, you will get the largest odd number if there is one): "))
    if num%2 == 1:
        odd_flag = True 
        if largest_odd == None:
            largest_odd = num 
        elif largest_odd <= num:
            largest_odd = num
    count = count + 1
if odd_flag == False:
    print("no odd number was entered")
else:
    print("the largest odd number is", largest_odd)

# suggested code from chatgpt
# Program to find the largest odd number among 10 user inputs
# count = 0
# largest_odd = None  # Variable to track the largest odd number

# while count < 10:
#     # Prompt the user for an integer
#     num = int(input("Enter an integer (10 inputs in total): "))
    
#     # Check if the number is odd
#     if num % 2 == 1:
#         # Update largest_odd if it's the first odd or larger than the current largest_odd
#         if largest_odd is None or num > largest_odd:
#             largest_odd = num
#     count += 1  # Increment the counter

# # Check if any odd number was entered
# if largest_odd is None:
#     print("No odd number was entered.")
# else:
#     print("The largest odd number is:", largest_odd)