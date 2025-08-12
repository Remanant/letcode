print("Wel come to the game treasure.\nChoose the route wisely to get the treasure, otherwise you'll be a loner like you're rn\nDon't even think about fighting monsters because you dont have 'that'")
print("Left = L, Right = R, Y = Yes, N = No (its not case sensitive so you can chill)")
direction = input("choose how do you want to proceed, go left or right: ").upper()

valid_input = (direction in ['L','R'])
if valid_input:
    if direction == "L":
        print("YOU DIED lol (a monster killed you)")
    else:
        print("you survived, but dont be happy too much just because you did'nt take L")
        actions = input("there is a black door in front of you.\ndo you want to open it?: ").upper()
        if actions == "N":
            print("YOU DIED (you waited too long.....the monster came)")
        elif actions == "Y":
            sword = input("There is a sword in the room, do you wanna pick it up and fight that thing?: ").upper()
            if sword == "Y":
                print("YOU DIED (I told you to not fight that thing because you don't have 'that'")
            else:
                print("good job ignoring the sword and getting out of there, here is your treasure ")
        else:
            print("wrong input")
else:
    print("wrong input")