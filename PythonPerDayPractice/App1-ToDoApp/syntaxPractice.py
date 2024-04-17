# checking all attributes existing in list
print(dir(list))

todos = []

# iterating in while loop, to continuously take inputs from user
while True:
    
    # taking input from user
    user_input = input("Choose your option (add, show or exit): ")
    
    # removing trailing whitespaces from string
    user_input = user_input.strip()

    # applying match-case for app functionality
    match user_input:

        # adding task
        case 'add':
            todo = input("add a todo: ")
            todos.append(todo)
        
        # showing or displaying task ("|" it is a bitwise OR operator)
        case 'show' | 'display':
            for item in todos:
                item = item.title()
                print(item)
        
        # exiting from iteration        
        case 'exit':
            print("Bye!")
            break

        # edit option -> replace an existing text with new text at a specific location in list
        case 'edit':
            number = int(input("Enter text position you want to edit: ")) - 1
            todos[number] = input("Enter new text to be replaced: ")

        # Irrefutable Pattern Handling: when user entering an unknown text (we can use any variable name in this case)
        case _ :
            print("Hey, you entered an unknown text. Please insert (add/show/exit)")