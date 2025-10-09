# Password generator using function
# Creates, displays, and saves passwords to a file.

import random
save_file="pass_saves.txt"

#Creating the data from which the password would be created:

small=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
cap=["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
sym=["~","!","@","#","$","%","^","&","*","/","?","."]
num=["0","1","2","3","4","5","6","7","8","9"]
all_char=sym+cap+num+small

# Creating file to store the passwords

with open("pass_saves.txt",'w') as file:
     file.write("Your Passwords: ")

# Creating the function to create and store the passwords
def password_generator():
            while True:
                password=""
                length=int(input("Enter the length of password needed [4],[8],[16]: "))
                while length not in[4,8,16]:
                    print("Invalid Choice. Try Again")
                    length=int(input("Enter the length of password needed [4],[8],[16]: "))

                for i in range(length):
                    b1=random.choice(all_char)
                    password+=b1
                
                print(password)

                with open("pass_saves.txt",'a') as file:
                     file.write(password)
                     file.write("\n")
                
                view_choice1=input("Enter 'v' to view the passwords or 'p' for more passwords: ")
                while view_choice1 not in ['v','p']:
                     print("Invalid Choice")
                     view_choice1=input("Enter 'v' to view the passwords or 'p' for more: ")

                if view_choice1=="v":
                     with open("pass_saves.txt",'r') as file:
                          view=file.read()
                          print(view)
                     break
                elif view_choice1=="p":
                       password1=""
                       length1=int(input("Enter the length of password needed [4],[8],[16]: "))
                       while length1 not in[4,8,16]:
                            print("Invalid Choice. Try Again")
                            length1=int(input("Enter the length of password needed [4],[8],[16]: "))
                       for i in range(length1):
                            b1=random.choice(all_char)
                            password1+=b1
                       print(password1)
                       with open("pass_saves.txt",'a') as file:
                        file.write(password1)
                        file.write("\n") 

                       view_choice2=input("Enter 'v' to view the passwords or 'e' to exit ")
                       while view_choice2 not in ['v','e']:
                               print("Invalid Choice. Try Again \n")
                               view_choice2=input("Enter 'v' to view the passwords or 'e' to exit ")
                       if view_choice2=="v":
                           with open("pass_saves.txt",'r') as file:
                            view=file.read()
                            print(view)
                            break
                       elif view_choice2=="e":
                            print("Goodbye")
                            break
                       else:
                           print("Invalid Choice")
                           break
                else:
                     print("Invalid Choice\n end")
                     break
                        
# The start of the program

print("Welcome to password Generator\n")
user_start=int(input("\nPress [1] to start: \n"))

if(user_start==1):
    password_generator()  
elif(user_start!=1):
   exit_choice=input("Do you want to exit?\n [y] / [n]: \n")
   while True:
       if (exit_choice=="y"):
               print("Goodbye")
               break
       elif (exit_choice=="n"):
               user_start=int(input("\nPress [1] to start: \n"))
               if(user_start==1):
                    password_generator()
               else:
                    print("Why Brother . Just Start this or end this")
                    print("please restart")
                    break
       else:
           print("Invalid Choice. Try Again \n")
else:
    print("Invalid Choice. Try Again \n")

  
