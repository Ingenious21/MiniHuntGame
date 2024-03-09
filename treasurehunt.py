print("Treasure Hunt Game\n")
name = input("Please enter player's name: ")
print(f"Welcome, {name}! Now let's begin our adventure to find the hidden treasure(s).")

print("You are before a lake. To get across, you have to wait for a boat or swim across the lake.\n")
ipt1 = input("Enter 'wait' to wait for a boat or 'swim' to swim across the lake: ")
print()
if ipt1.lower() == "wait":
    print("You crossed the lake using a boat.")
    print("You have reached a house with three doors of the following colors: Red, Yellow, and Green.")
    ipt2 = input("Which door do you want to go through? Enter the color of the door: ")
    print()

    if ipt2.lower() == "red":
        print("You have found the treasure.\n Congratulations!")
    elif ipt2.lower() == "yellow":
        print("You have entered a wrong door and got eaten by a monster.\n Game over!")
    elif ipt2.lower() == "green":
        print("You have entered a wrong door and got eaten by a monster.\n Game over!")
    else:
        print("Wrong entry. Please restart the game.")

elif ipt1.lower() == "swim":
    print("You had love for the game, but did not make it. LOL")

else:
    print("Wrong entry. Please restart the game.")
