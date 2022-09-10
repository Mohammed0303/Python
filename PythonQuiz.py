#IT quiz program with simple 5 questions

print("Welcome to my computer quiz!")

playing = input("\nDo you want to play!(yes/no): ")

if playing != "yes":
    quit()

print("Okay! Let's play")
score = 0

answer = input("1.What does CPU stands for?: ")
if answer.lower() == "central processing unit":
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")

answer = input("\n2.What does RAM stands for?: ")
if answer.lower() == "random access memory":
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")

answer = input("\n3.What does GPU stands for?: ")
if answer.lower() == "graphics processing unit":
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")

answer = input("\n4.What does PSU stands for?: ")
if answer.lower() == "power supply":
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")

answer = input("\n5.What does ROM stands for?: ")
if answer.lower() == "read only memory":
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")



