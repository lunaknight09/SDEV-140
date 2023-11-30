##Midterm Exam
##November 22, 2023
##Nathan Hopkins

##We are to display to customer what we are asking them to do
def display_menu():
    print("\nTask Management Program")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Quit")

##If add_task selected we want to give them a notification that the task as been added properly into the program
def add_task(task_list):
    task = input("Enter the task: ")
    if task:
        task_list.append(task)
        print("Task added successfully!")
    else:
        print("Error: Task cannot be empty.")

##If display_tasks is selected we want to show the tasks added in are in the proper order they were added
def display_tasks(task_list):
    if not task_list:
        print("No tasks to display.")
    else:
        print("\nTask List:")
        for index, task in enumerate(task_list, 1):
            print(f"{index}. {task}")

##We want to direct the customer to the choice needed either it be to add or display the tasks entered
##If this was not displayed to show what the ask is then we would receive more errors than needed
##Adding the function of quit this gives then however many loops of the tasks they need to put in being infinite until they are done
def main():
    tasks = []

    while True:
        display_menu()

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            print("Quitting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()