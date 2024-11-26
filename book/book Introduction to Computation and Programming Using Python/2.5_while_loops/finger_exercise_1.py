# num_x = int(input("how many times should i print the letter x? "))
num_x = 3
to_print = ""
# concatenate x to to_print num_x times
count = 0
# repeat the code inside while the test conditional is True 
while count < num_x:
    to_print = to_print + "x"
    count = count + 1
print(to_print)

# visualize 
# translate while loop to pure conditionals 
# python tutor can tell both the while loop above and the pure conditionals 
# below run 14 steps 
num_x = 3
to_print = ""
count = 0
if count < num_x:
    to_print = to_print + "x"
    count = count + 1
# print(to_print)
# print(count)
if count < num_x:
    to_print = to_print + "x"
    count = count + 1
# print(to_print)
# print(count)
if count < num_x:
    to_print = to_print + "x"
    count = count + 1
    # print("i will appear if i am running")
# print(to_print)
# print(count)
if count < num_x:
    to_print = to_print + "x"
    count = count + 1
    print("i will appear if i am running")
print(to_print)
# print(count)