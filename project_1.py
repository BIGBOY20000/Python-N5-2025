name = input("Please enter your name: ")
if name == "Kevin":
    numberofbadges = int(input("Please enter the number of badges you want: "))
    if numberofbadges < 0.0:
        print("Goofy boy you cant have 0")
    elif numberofbadges >= 150:
        print("your order will cost" + str((numberofbadges/100 * 90)/4))
    