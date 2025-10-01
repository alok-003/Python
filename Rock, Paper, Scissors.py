# Rock, Paper, Scissors
import random
set=("rock","paper"," scissors")
a=random.choice(set)

print("Welcome to Rock, Paper, Scissors")
in1=int(input("Press (1) to start"))
if(in1!=1):
    print("Goodbye")
else:
    in2=input("Enter Your Choice:").lower()
    if(in2==a):
        print("Tie")
    elif (a=='scissors' and in2=="rock"):
        print("Rock beat Scissors. You Win!")
    elif (a=='scissors' and in2=="paper"):
        print("Scissors beat Paper . You Lose !")
    elif (a=='rock' and in2=="paper"):
        print("Paper beat Rock . You Win !")
    elif (a=='rock' and in2=="scissors"):
        print("Rock beat Scissors . You Lose !")
    elif (a=='paper' and in2=="scissors"):
        print("Scissors beat Paper . You Win !")
    elif (a=='paper' and in2=="rock"):
        print("Paper beat Rock . You Lose !")
    else:
        print("Invalid Choice\nGoodbye")


