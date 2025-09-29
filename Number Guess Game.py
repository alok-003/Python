import random
a= random.randrange(1,10)
print("Guess The Number")
in1=int(input("Enter 1 to play the Game"))
if(in1==1):
    in2=int(input("Guess The Number"))
    while(in2!=a):
        print("Incorrect Guess \n Try Again")
        in2=int(input("Guess The Number"))
    print("Correct Guess")
else:
    print("Goodbye")    