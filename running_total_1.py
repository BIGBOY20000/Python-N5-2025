#task 1 

#Create a program that simulates a savings plan. 
#Ask the user to input monthly savings amounts for a year (12 months) and display the running total after each input.

total=0 

for index in range(12):
    savings = float(input("Enter the monthly saving amount (£): "))

    total = total + savings

print("the total saving amount after one year is", total)