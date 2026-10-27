task = []
while True:
    print("WELCOME to TO - DO LIST")
    print("1.  Add Task")
    print("2.  View Task")
    print("3.  Exit")

    try:
        choice = int(input("enter your choice : "))
    except ValueError:
        print("please enter a valid number")
        continue

    print("you selected : ", choice)

    if choice == 1 :
        print("Add Task selected")
        new = input("enter  task separated by commas : ")
        for i in new.split(","):
            task.append(i.strip())
        print("Task added successfully!")
    elif choice == 2:
        print("View Task selected")
        if len(task) == 0:
            print("task is not available ")
        else:
            print("your task:- ")
            for i,t in enumerate(task,start=1):
                print(i," .",t)
    elif choice == 3:
        print("EXIT SELECTED")
        print("THANK YOU FOR USING TO - DO LIST")
        break
    else:
        print("invalid choices! please select 1, 2 or 3.")



