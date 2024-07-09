print("Welcome to Mihwa's mini game")

answer = input("Do you want to play? ")

if answer.lower() != "yes":
    quit()

score = 0
print("Okay! Let's play:-) ")

quiz1 = input("What does CPU stand for? ")
if quiz1.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

quiz1 = input("What does GPU stand for? ")
if quiz1.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

quiz1 = input("What does RAM stand for? ")
if quiz1.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

quiz1 = input("What does PSU stand for? ")
if quiz1.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print("You got "+str(score)+" corrected answer.")
print("You got "+str((score / 4) * 100)+" %")