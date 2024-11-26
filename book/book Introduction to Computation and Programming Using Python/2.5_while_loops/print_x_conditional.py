num_x = int(input("how many times should i print the letter x? "))
to_print = ""
if num_x == 1:
    to_print = "x"
elif num_x == 2:
    to_print = "xx"
elif num_x == 3:
    to_print = "xxx"
print(to_print)