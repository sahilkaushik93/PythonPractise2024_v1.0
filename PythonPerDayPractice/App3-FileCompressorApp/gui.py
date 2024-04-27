import sys
sys.path.append('E:\Job & Interview Kit\Revision Material\DS & Algos - Python & JavaScript\PythonPractise2024\PythonPerDayPractice')
import utilities
import FreeSimpleGUI as sg # for documentation search PySimpleGUI

# elements
label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output")

# window instance
window = sg.Window("File Compressor", layout=[[label1, input1, choose_button1],
                                              [label2, input2, choose_button2],
                                              [compress_button, output_label]])

# using the window instance, opening the app & performing actions
while True:
    event, values = window.read()
    print("event:",event)
    print("values:",values)
    print("file: ", values['files'].split(";"))
    utilities.make_archive(filepaths=values['files'].split(";"), dest_dir=values['folder'])
    window['output'].update(value = "Compressed Successfully!")

    # closing the window instance
    if sg.WIN_CLOSED:
        exit()

