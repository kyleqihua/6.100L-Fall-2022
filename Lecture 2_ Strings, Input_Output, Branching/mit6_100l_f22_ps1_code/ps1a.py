## 6.100A PSet 1: Part A
## Name: Kyle Huang
## Time Spent:
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Please enter you starting yearly salary: ")) 
print(yearly_salary)
portion_saved = float(input("Please enter the portion of salary to be saved: "))
cost_of_dream_home = float(input("Please enter the cost of your dream home: "))
#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25
amount_saved = 0
r = 0.05 


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
total_down_payment = cost_of_dream_home * portion_down_payment
monthly_saved_salary = (yearly_salary/12) * portion_saved 
amount_saved = amount_saved + monthly_saved_salary
