rightnumber = 8
guess = 1
number = int(input("Guess a number: "))
while (guess < 5) and (number != rightnumber):
  print("Not right. Try again.")
  guess = guess + 1
  number = int(input("Guess a number:"))
