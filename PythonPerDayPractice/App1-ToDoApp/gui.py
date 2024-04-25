import utilities
import FreeSimpleGUI as sg

# creating elements
label = sg.Text("Type in a to do:")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

# creating a window instance
# layout = "[]" elements in sq brackets will be kept on same row
window = sg.Window("My To-Do APP", layout=[[label], [input_box,add_button]]) 

# displaying GUI
window.read()

# displaying hello once GUI functions are performed
print('hello')

# closing instances & GUI
window.close()




