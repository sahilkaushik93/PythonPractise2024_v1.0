import sys
sys.path.append('E:\Job & Interview Kit\Revision Material\DS & Algos - Python & JavaScript\PythonPractise2024\PythonPerDayPractice')
import utilities
import FreeSimpleGUI as sg

# creating elements
label1 = sg.Text("Type in a to do:")
input_box1 = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

label2 = sg.Text("List of all to do tasks:")
input_box2 = sg.Listbox(values=utilities.read_todos(), key="todos",
                        enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")


layout = [
    [label1], 
    [input_box1],
    [label2],
    [input_box2],
    [add_button, edit_button, complete_button, exit_button]
]

# creating a window instance
# layout = "[]" elements in sq brackets will be kept on same row
window = sg.Window("My To-Do APP", 
                   layout=layout,
                   font=('Helvetica', 10)) 


# iterating to add multiple value via app
while True:
    # displaying GUI
    event, values = window.read()

    # event looks like a tuple containing value added in dict format
    print("1-event: ",event) # event at which value was added (added due to input_button)
    print("2-value: ", values) # value added with a key of "todo" (key given in input_button definition)
    print("3-current todos value selected: ", values)
    print("\n____________\n")

    # matching event and adding diff functionalities on to do app
    match event:
        
        case "Add":
            # adding add functionality [adding todos.txt in background]
            todos = utilities.read_todos()
            print("read todos: ", todos)

            # [Bug]:if todos.txt has no task it should not enter "\n" in that case
            if not values['todo']:
                new_todo = values['todo']
            else:
                new_todo = values['todo'] + "\n"
            
            todos.append(new_todo)
            print("new todos: ",todos)
            
            utilities.write_todos(todos)

            # making things appear live by updating values in windows instance
            window["todos"].update(values=todos)

        case "Edit":
            # adding edit functionality [updating todos.txt in background]
            todos = utilities.read_todos()

            edit_todo = values['todos'][0]
            edit_index = todos.index(edit_todo)
            new_todo = values['todo'] + "\n"
            todos[edit_index] = new_todo
            
            utilities.write_todos(todos)

            # making things appear live by updating values in windows instance
            window["todos"].update(values=todos)

        case "todos":
            # to show selected to do item from list box into input box 1 (key='todo')
            window['todo'].update(value=values['todos'][0])

        case "Complete":
            todos = utilities.read_todos()
            print("read todos: ", todos)
            val = values['todos'][0]
            print("val:", val)
            # val_index = todos.index(val)
            # todos.pop(val_index)
            todos.remove(val)
            print("write todos:", todos)
            utilities.write_todos(todos)

            # making things appear live by updating values in windows instance
            window["todos"].update(values=todos) # changes will appear in list box
            window["todo"].update(value='') # changes will apear in input box

        case "Exit":
            exit()

        case sg.WIN_CLOSED:
            break

 
    

# displaying hello once GUI functions are performed
print('hello')

# closing instances & GUI 
window.close()




