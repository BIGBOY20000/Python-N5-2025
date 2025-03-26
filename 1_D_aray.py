scores = [75, 82, 93, 65, 78]
highestScore = scores[0]
for index in range (1,(scores)):
    if scores[index] > highestScore:
        highestScore = scores[index]
    
print("The highest score is", highestScore) 