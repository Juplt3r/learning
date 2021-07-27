import random
import os 

Answer = random.randint(0, 100)
print(Answer)

MinNo = 0
MaxNo = 100
win = False
os.system("cls")
while win != True:
    print("Guess a Number between", MinNo,"to",MaxNo)
    Guess = int(input())
    if MaxNo < Guess or Guess < MinNo:
        os.system("cls")
        print("Invalid Input, Please Try Again")
    else:
        if Guess < Answer:
            os.system("cls")
            print("Incorrect!")
            MinNo = Guess
        elif Guess > Answer:
            os.system("cls")
            print("Incorrect!")
            MaxNo = Guess
        elif Guess == Answer:
            os.system("cls")
            print("Congrats! The Correct Answer is", Guess)
            win = True