temp = []
for index in range(5):
    temp = float(input("Enter temperature between -20 and 50°C: "))
    while temp < -20 or temp > 50:
        temp = float(input("Invalid input, enter a temperature between -20 and 50°C: "))
temp.append(temp)