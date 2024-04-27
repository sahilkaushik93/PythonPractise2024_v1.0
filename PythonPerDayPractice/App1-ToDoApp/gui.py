## Import Libraries
# sys to access "utilities.py" present in some other folder structure
# "utilities" to access all supporting utility functions
# "FreeSimpleGUI" to create Desktop App Interface ("PySimpleGUI" is paid version of "FreeSimpleGUI")
# "time" to add displaying time feature on APP
import sys
sys.path.append('E:\Job & Interview Kit\Revision Material\DS & Algos - Python & JavaScript\PythonPractise2024\PythonPerDayPractice')
import utilities
import FreeSimpleGUI as sg
import time

# Applying theme (go on google & search "PySimpleGUI themes images")
sg.theme("Reds")

# logo paths
img_loc = './PythonPerDayPractice/App1-ToDoApp/assets/images'
add_img = f'{img_loc}/add.png'
add_img2 = f'./PythonPerDayPractice/App1-ToDoApp/add.png'
edit_img = f'{img_loc}/edit.png'
complete_img = f'{img_loc}/complete.png'
exit_img = f'{img_loc}/exit.png'

# creating window elements
now = time.strftime("%b %d, %Y %H:%M:%S")
clock = sg.Text(key="clock")
label1 = sg.Text("Type in a to do:")
input_box1 = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(size=2, image_source=add_img, key="Add", tooltip="Add Task.", mouseover_colors="Grey")

label2 = sg.Text("List of all to do tasks:")
input_box2 = sg.Listbox(values=utilities.read_todos(), key="todos",
                        enable_events=True, size=[45,10])
edit_button = sg.Button(size=2, image_source=edit_img, key="Edit", tooltip="Edit Task.", mouseover_colors="Grey")
complete_button = sg.Button(size=2, image_source=complete_img, key="Complete", tooltip="Mark Task Complete.", mouseover_colors="Grey")
exit_button = sg.Button(size=2, image_source=exit_img, key="Exit", tooltip="Exit App.", mouseover_colors="Grey")

# giving layout of elements to be displayed in windows 
layout = [
    [clock],
    [label1], 
    [input_box1],
    [label2],
    [input_box2],
    [add_button, edit_button, complete_button, exit_button]
]

# creating a window instance
# layout = "[]" elements in sq brackets will be kept on same row
window = sg.Window("My To-Do APP", layout=layout, font=('Helvetica', 10)) 


# iterating to add multiple value via app
while True:
    # displaying GUI
    event, values = window.read(timeout=100)

    # displaying clock on window
    window["clock"].update(value=now)

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
            
            todos.append(f"{now} : {new_todo}")
            print("new todos: ",todos)
            
            utilities.write_todos(todos)

            # making things appear live by updating values in windows instance
            window["todos"].update(values=todos)

        case "Edit":
            # adding edit functionality [updating todos.txt in background]
            todos = utilities.read_todos()

            try:
                edit_todo = values['todos'][0]
                edit_index = todos.index(edit_todo)
                new_todo = values['todo'] + "\n"
                todos[edit_index] = new_todo
                
                utilities.write_todos(todos)
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 10))

            # making things appear live by updating values in windows instance
            window["todos"].update(values=todos)

        case "todos":
            # to show selected to do item from list box into input box 1 (key='todo')
            window['todo'].update(value=values['todos'][0])

        case "Complete":
            
            try:
                todos = utilities.read_todos()
                print("read todos: ", todos)
                val = values['todos'][0]
                print("val:", val)
                # val_index = todos.index(val)
                # todos.pop(val_index)
                todos.remove(val)
                print("write todos:", todos)
                utilities.write_todos(todos)
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 10))    

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




