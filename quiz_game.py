print("Welcome to my computer quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the capital of Texas ")
if answer.lower() == "austin":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("Does does VFR stand for? ")
if answer.lower() == "visual flight rules":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

    
answer = input("What does PLC stand for? ")
if answer.lower() == "programmable logic control":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " questions correct!")
print("You got a " + str((score/4) *100) + "%")