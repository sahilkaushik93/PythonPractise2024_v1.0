# checking all attributes existing in list
# print(dir(list))

todos = []

# reading todos.txt file
with open('./PythonPerDayPractice/App1-ToDoApp/todos.txt',"r") as file1:
    todos1 = file1.readlines()
file1.close()

# writing in the txt file
file2 = open('./PythonPerDayPractice/App1-ToDoApp/todos.txt',"w")

# iterating in while loop, to continuously take inputs from user
while True:
    
    # taking input from user
    user_input = input("Choose your option (add, show, edit, complete or exit): ")
    
    # removing trailing whitespaces from string
    user_input = user_input.strip()

    # applying match-case for app functionality
    match user_input:

        # adding task
        case 'add':
            todo = input("add a todo: ") + "\n" 
            todos1.append(todo)
            file2.writelines(todos1)
        
        # showing or displaying task ("|" it is a bitwise OR operator)
        case 'show' | 'display':
            for index, item in enumerate(todos1):
                item = item.title().strip("\n")
                print(f"{index+1}-{item}")
        
        # exiting from iteration        
        case 'exit':
            print("Bye!")
            file2.close()
            break

        # edit option -> replace an existing text with new text at a specific location in list
        case 'edit':
            number = int(input("Enter text position you want to edit: ")) - 1
            todos1[number] = input("Enter new text to be replaced: ") + "\n"
            file2.writelines(todos1)

        # complete option -> ask for task no & remove the task i.e. completed
        case 'complete':
            number = int(input("Enter text position you want to mark complete: ")) - 1
            todos1.pop(number)
            file2.writelines(todos1)

        # Irrefutable Pattern Handling: when user entering an unknown text (we can use any variable name in this case)
        case _ :
            print("Hey, you entered an unknown text. Please insert (add/show/exit)")