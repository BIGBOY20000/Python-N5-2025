#Create a simple text-based adventure game called "The Mystery Mansion" where players can explore four different locations.

#Your program must demonstrate understanding of 1D arrays, input validation, and string concatenation
##Your adventure takes place in a mysterious mansion with these four rooms:

#Entrance Hall - "A grand foyer with a crystal chandelier"
#Library - "Dusty bookshelves stretch from floor to ceiling"
#Kitchen - "Copper pots hang above an old stone hearth"
#Garden - "Overgrown vines twist around marble statues"


locations = ("Entrance Hall", "Library", "Kitchen", "Garden")
descriptions = (
    "A grand foyer with a crystal chandelier.",
    "Dusty bookshelves stretch from floor to ceiling.",
    "Copper pots hang above an old stone hearth.",
    "Overgrown vines twist around marble statues.")

commands = ("N", "S", "E", "W", "help", "quit")
            
current_location = 0 


print("Welcome to The Mystery Mansion!")
name = input("What is your name? ")
print("Hello, " + name + "! Let's begin your adventure...")

playing = True
while playing:
    print("You are in the " + locations(current_location) + " - " + descriptions(current_location))
    move = input("Enter a command (N, S, E, W, help, quit): ").upper()

    if move == "HELP":
        print("Commands: N, S, E, W, help, quit")
    elif move == "QUIT":
        print("Goodbye, " + name + "!")
        playing = False
    elif move not in commands:
        print("That is not a valid command.")
    else:
        if location == 0 and move == "E":
            location = 1
        elif location == 0 and move == "S":
            location = 2
        elif location == 1 and move == "W":
            location = 0
        elif location == 1 and move == "S":
            location = 3
        elif location == 2 and move == "N":
            location = 0
        elif location == 2 and move == "E":
            location = 3
        elif location == 3 and move == "N":
            location = 1
        elif location == 3 and move == "W":
            location = 2
        else:
            print("You can't go that way.")