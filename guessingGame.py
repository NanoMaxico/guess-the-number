import random
guessNum = random.randint(1,9)

print("guess a number between 1 to 9")
guessedNum = input("guess the number")


if(guessedNum<guessNum):
    print("the number is higher than ",guessNum)
    
elif(guessedNum>guessNum):
    print("the number is lower than ",guessNum)
    
else:
    print("YOU WIN")