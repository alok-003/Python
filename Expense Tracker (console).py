# Expense Tracker (console)

expenses=[]

print("Welcome to expense Tracker")

in1=int(input("\nPress [1] to start: \n"))
if in1!=1:
    print("Goodbye\nThanks")
else:
    while True:
        in2=int(input("What do you want to do:\n[1] Add \n[2] Remove \n[3] View \n[4] Exit: \n"))
        if(in2==1):
            add1=float(input("Enter the amount to add: "))
            cat1=input("Enter the Category: ")
            dat1=input("Enter the date: " )
            expense={"Amount":add1,"Category":cat1,"Date":dat1}
            expenses.append(expense)
            print(expenses,"\n")
        elif(in2==2):
            if len(expenses)=="0":
                print("\nNo expenses to remove")
            else:
                print(expenses,"\n")
                rem1=int(input("\nEnter the index no of the transactionto delete: "))
                del expenses[rem1]
                print(expenses,"\n")
        elif(in2==3):
            print(expenses,"\n")
        elif(in2==4):
            print("\nGoodbye")
            break
        else:
            print("\nInvalid Choice")
            print("Restart")
            break
    
