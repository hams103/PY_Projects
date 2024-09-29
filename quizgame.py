


## PYTHON QUIZ
## INTRO
# -------------------------------------------------
print("welcome")
playing = input("Do you want to play? ")

if playing.upper() != "YES":
    quit()

print("Okay! Let's play!")
score = 0
count = 0
# -------------------------------------------------

## QUESTION-1
# -------------------------------------------------
answer = input("What does CPU stand for? ")

if answer.upper() == "CENTRAL PROCESSING UNIT":
    print('Correct!')
    score += 1
    count += 1
else:
    print('Incorrect!')
    count += 1
# -------------------------------------------------

## QUESTION-2
# -------------------------------------------------
answer = input("What does GPU stand for? ")

if answer.upper() == "GRAPHICS PROCESSING UNIT":
    print('Correct!')
    score += 1
    count += 1
else:
    print('Incorrect!')
    count += 1
# -------------------------------------------------

## QUESTION-3
# -------------------------------------------------
answer = input("What does RAM stand for? ")

if answer.upper() == "RANDOM ACCESS MEMORY":
    print('Correct!')
    score += 1
    count += 1
else:
    print('Incorrect!')
    count += 1
# -------------------------------------------------


## QUESTION-4
# -------------------------------------------------
answer = input("What does PSU stand for? ")

if answer.upper() == "POWER SUPPLY":
    print('Correct!')
    score += 1
    count += 1
else:
    print('Incorrect!')
    count += 1
# -------------------------------------------------

## prints score and count
print("You got " + str(score) + " questions correct. Out of " + str(count) + " total questions")

## prints %
sum = (score/count)*100
print(str(sum) + "% Correct")