# To-Do List (console)

Task=[]
print("Welcome to To-Do List!\n")

while True:
    print("Tasks:",Task)
    a=int(input("\nPress \n[1]Add Task \n[2]View Task \n[3]Remove Task \n[4]Exit\n\n"))
    if(a==1):
        task_add=input("\nEnter The Task to add: ")
        Task.append(task_add)
        print("Task Added Successfully")
        print("Tasks:",Task)
    elif(a==2):
        task_view=print("Tasks:",Task)
    elif(a==3):
        task_rem=input("\nEnter the task to remove: ")
        Task.remove(task_rem)
        print("Task Removed Successfully")
        print("Tasks:",Task)
    elif(a==4):
        print("Thank You \nGoodbye")
        break
    else:
        print("\n\nInvalid Choice \nTry Again\n")
        
