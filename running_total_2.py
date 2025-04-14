#task 2 

#Create a program that asks the user to input 5 test scores and calculates the running total after each input.

total = 0 

for index in range(0, 5):
    score = float(input("Enter score: "))

    total += score

    print("Running total after score:", total)