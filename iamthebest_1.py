
list= []

#get user input
percentage = int(input("Enter percentage"))

#Validate between 0 and 100
while percentage < 0 or percentage > 100:
    print("Error, % must be between 0 and 100")
    percentage = int(input("please enter a valid percentage"))

    list.append(percentage)
    print(list)