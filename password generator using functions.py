# Password generator using function
# Creates, displays, and saves passwords to a file.

import random

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
                for i in range(length):
                    b1=random.choice(all_char)
                    password+=b1

                print(password)

                with open("pass_saves.txt",'a') as file:
                     file.write(password)
                     file.write("\n")
                
                view_choice=input("Enter 'v' to view the passwords or 'p' to proceed: ")
                while True:
                    if view_choice=="v":
                         with open("pass_saves.txt",'r') as file:
                              view=file.read()
                              print(view)
                              break
                    elif view_choice=="p":
                         print("Next Step: ")
                         break
                    else:
                         print("Invalid Choice")
                         break
               
                pass_repeat=input("\nDo you want another password? (y/n): ")
                if pass_repeat=="n":
                    print("Goodbye")
                    break

# The start of the program

print("Welcome to password Generator\n")
user_start=int(input("\nPress [1] to start: \n"))
if(user_start!=1):
   print("End\nGoodbye")
else:

   password_generator()   
