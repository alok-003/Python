import random
small=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
cap=["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
sym=["~","!","@","#","$","%","^","&","*","/","?","."]
num=["0","1","2","3","4","5","6","7","8","9"]
all_char=sym+cap+num+small


print("Welcome to Password Generator")
in1=int(input("Press [1] to start: "))
if(in1!=1):
    print("Thank you\nGoodbye")
else:
    while True:
        password=""
        length=int(input("Enter the length of password needed [4],[8],[16]: "))
        for i in range(length):
            b1=random.choice(all_char)
            password+=b1
        print(password,end="")
        in2=input("\nDo you want another password? (y/n): ")
        if in2=="n":
            break     