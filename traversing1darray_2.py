#Task 2
#Create a program that contains an array of 5 dog food weights (in grams) between 0 and 300g.
# Traverse the 1D array to calculate and display the total amount of food given to the dog over 5 days.

dog_food_weights = [250, 200, 275, 180, 300]
total_food = 0
for weight in dog_food_weights:
    total_food += weight
print("Total dog food given over 5 days:", total_food, "grams")
