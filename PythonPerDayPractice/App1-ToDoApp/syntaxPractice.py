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
        
        # showing or displaying task    
        case 'show' | 'display':
            for item in todos:
                print(item)
        
        # exiting from iteration        
        case 'exit':
            print("Bye!")
            break

        # when user entering an unknown text (we can use any variable name in this case)
        case _ :
            print("Hey, you entered an unknown text. Please insert (add/show/exit)")