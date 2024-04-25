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


layout = [
    [label1, input_box1, add_button],
    [label2],
    [input_box2, edit_button]
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
    print("event: ",event) # event at which value was added (added due to input_button)
    print("value: ", values) # value added with a key of "todo" (key given in input_button definition)

    match event:
        case "Add":
            # adding add functionality [updating todos.txt in background]
            todos = utilities.read_todos()
            new_todo = values['todo']
            todos.append(new_todo)
            utilities.write_todos(todos)

            # making things appear live by updating values in windows instance
            window["todos"].update(values['todo'])

        case "Edit":
            print(values)
        case sg.WIN_CLOSED:
            break

 
    

# displaying hello once GUI functions are performed
print('hello')

# closing instances & GUI 
window.close()




