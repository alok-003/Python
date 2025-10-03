import random
print("Virtual dice")
in1=int(input("Press 1 to roll the dice: "))
if(in1!=1):
    print("Goodbye")
else:
    while True:
        c=random.randint(1,6)
        print(c)
        in2=int(input("press (1) to roll again: "))
        if(in2!=1):
            print("Goodbye")
            break