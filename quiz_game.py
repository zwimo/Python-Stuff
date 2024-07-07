print("Welcome to Zach's Quiz")

playing = input("Do you want to play a game? ")

if playing.lower() != "yes":
    quit()
    
print("Alrighty! :D ")
score = 0

answer = input("What is the capital of Kansas? ")
if answer.lower() == "topeka":
    print('Right!')
    score += 1
else:
    print("Wrong!")
    
answer = input("What city in Kansas has the largest population? ")
if answer.lower() == "wichita":
    print('Right!')
    score += 1
else:
    print("Wrong!")

answer = input("What is the state bird of Kansas? ")
if answer.lower() == "meadowlark":
    print('Right!')
    score += 1
else:
    print("Wrong!")

print("You got " + str(score) + " questions right!")
print("Which is " + str((score/4) * 100) + " %.")


