name = input("Type your name: ")
print("Welcome", name, "to this adventure!")
answer = input("You are traveling wild area. It has come to an end and you can go left or right. Which way would you like to go? ")

if answer == "left":
    answer = input("You come to a creek. You can walk around it or take boat. walk/boat ")

    if answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    elif answer == "boat":
        answer = input("While traveling by boat, you saw an island. Do you want to discover this area? yes/no ")
        if answer == "yes":
            print("You met tigers in this area. You lost the game.")
        else:
            print("You traveled by boat and were eaten by alligators.")
    else:
        print("Not a valid option. You lose.")


elif answer == "right":
    answer = input("You come to a brigde, it looks wobbly, do you want to cross it or head back (cross/back) ")
    if answer == "cross":
        answer= input("You cross the bridge and meet a stranger. Do you want to talk with? (Y/N)")
        if answer == "Y":
            print("You talk to the stranger and they give you medal. YOU WIN")
        elif answer == "N":
            print("You ignore the stranger and they attacked. You lost the game. ")
        else:
            print("Not a valid option. You lose.")

    elif answer == "back":
        print("You go back and lose.")
    else:
        print("Not a valid option. You lose.")


print("Thank you for trying this game.")