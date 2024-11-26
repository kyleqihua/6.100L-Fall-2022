
# test if the pair of root and pwr exists. if not, print a message to that effect
# it is so hard to formalize my thoughts 
# num = int(input("enter an integer to test the existence of the pair: "))
# root = 2
# pwr = 2 
# pair_flag = False
# for pwr in range(2, 6):
#     if pow(root, 2) > num:
#         break 
#     root = root + 1
# for pwr in range(2, 6):
#     if pow(root, pwr) == num:
#         print("the pair exists. the root is", root, "and the pwr is", pwr)
#         pair_flag = True
#         break 
#     if pow(root, pwr) > num:
#         break 
# root = root + 1
# if pow(root, 2) > num:
#     break 
# if pair_flag == False:
#     print("the pair does not exist")
# while pow(root, pwr) <= num:

# for pwr in range(2, 6):
#     while pow(root, pwr) <= num:
#         if pow(root, pwr) == num:
#             print("the pair exists. the root is", root, "and the pwr is", pwr)
#             pair_flag = True
#             break 
#         root = root + 1


# after learning while and for loops for hours...
num = int(input("please enter an integer: "))
negative_flag = False
pair_flag = False 
if num < 0:
    negative_flag = True 
    num = -num 
for i_root in range(num):
    for i_pwr in range(2, 6):
        if pow(i_root, i_pwr) == num:
            if negative_flag:
                i_root = -i_root
            print("the root is", i_root, "and the pwr is", i_pwr)
            pair_flag = True 
if pair_flag == False:
    print("no such pair is found") 