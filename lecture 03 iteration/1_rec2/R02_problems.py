####################################################################################
# Practice Problem 1
# Write a program that takes your name as an Input and Outputs the length of your name minus 5.

# Insert code below
# name = input("please enter your name ")
# print(len(name) - 5)

####################################################################################
# Practice Problem 2
# Write a program to remove the nth character from a non empty string.
# Print the old string and the new string.

test_string = "We want to remove the nth character from this string"
n = 8

# Insert code below
# print("this is the old string:", test_string)
# new_string = test_string[0:n-1] + test_string[n:len(test_string)]
# print("this is the new string:", new_string)


####################################################################################
# Practice Problem 3
# Write a program which answers the following:
# Does a given string have length greater than 10 or less than 5? If True, output True. If False, output False.

my_string = "This is my string"  # example string - modify to test

# Insert code below
# if len(my_string) > 10 or len(my_string) < 5:
#     print(True)
# else:
#     print(False) 



####################################################################################
# Practice Problem 4
# Write a program which answers the following using a for loop:
# Count the number of e's in the following string

my_string = "How many times is the letter e in this string?"

# Insert code below
sum = 0
for i in my_string:
    if i == "e":
        sum = sum + 1
print(sum)




