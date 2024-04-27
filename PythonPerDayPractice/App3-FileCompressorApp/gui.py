import sys
sys.path.append('E:\Job & Interview Kit\Revision Material\DS & Algos - Python & JavaScript\PythonPractise2024\PythonPerDayPractice')
import utilities
import FreeSimpleGUI as sg # for documentation search PySimpleGUI

# elements
label1 = sg.Text("Select Source:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="Source")

label2 = sg.Text("Select Target:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="Target")

compress_button = sg.Button("Compress")
extract_button = sg.Button("Extract")
exit_button = sg.Button("Exit")
output_label = sg.Text(key="output", text_color="Red")

layout = [
    [label1, input1, choose_button1],
    [label2, input2, choose_button2],
    [compress_button, extract_button, exit_button, output_label]
    ]

# window instance
window = sg.Window("File Compressor", layout=layout)

# using the window instance, opening the app & performing actions
while True:
    event, values = window.read()
    print("event:",event)
    print("values:",values)
    

    match event:
        case "Compress":
            utilities.make_archive(filepaths=values['Source'].split(";"), dest_dir=values['Target'])
            window['output'].update(value = "Compressed Successfully!")
        case "Extract":
            utilities.extract_archive(archivepath=values['Source'], dest_dir=values['Target'])
            window['output'].update(value = "Extracted Successfully!")
        case "Exit":
            exit()
        case sg.WIN_CLOSED:
            exit()

    # # closing the window instance
    # if sg.WIN_CLOSED:
    #     exit()

