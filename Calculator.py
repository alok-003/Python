#Calculator

print("Welcome to Calculator")
in1=int(input("Press (1) to start "))
if(in1==1):
    a=float(input("Enter the first number: "))
    b=float(input("Enter the second number:"))
    c=int(input("What operation do you want to perform\n Addition(1)\n Subtraction(2)\n Multiplication(3)\n Division(4)"))
    if( c==1):
            print(a+b)
    elif(c==2):
            print(a-b)
    elif(c==3):
            print(a*b)
    elif(c==4):
        if(b!=0):
            print(a/b)
        else:
            print("Error: Division by Zero ")
    else:
        print("Invalid Choice\n Enter a Valid Choice")
else:
      print("Invalide choice\n Goodbye")
        