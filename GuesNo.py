import random
import os 

Answer = random.randint(1, 99)
print(Answer)

pts = 10

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
            pts -= 1
        elif Guess > Answer:
            os.system("cls")
            print("Incorrect!")
            MaxNo = Guess
            pts -= 1
        elif Guess == Answer:
            os.system("cls")
            print("Congrats! The Correct Answer is", Guess)
            if pts > 0:
                print("Final Score is", pts, "out of 10")
            else:
                print("Final Score is 0 out of 10")
            win = True