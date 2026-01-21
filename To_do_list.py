tasks = []

def add_task (task):
    tasks.append(task)

def show_task ():
    if not tasks:
        print("No Tasks Are Avelable")
    else:
        for i in range (len(tasks)):
            print(i+1, "." , tasks[i])

def remove_task(index):
    if index >= 0 and index < len(tasks):
        tasks.pop(index)

print("----TO DO LIST----")


while True:
    
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = int(input("Enter The Number : "))

    if choice == 1 :
        task = input("Enter Task : ")
        add_task(task)
    
    elif choice == 2:
        show_task()

    elif choice == 3:
        show_task()
        num = int(input("Enter That Number You Want To Remove : "))
        remove_task(num - 1)

    elif choice == 4:
        print("Exiting To Do List")
        break
    else :
        print("Invalede Choice")
