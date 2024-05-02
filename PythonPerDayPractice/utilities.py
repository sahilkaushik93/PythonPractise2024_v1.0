# utility functions
import zipfile
import pathlib
import smtplib, ssl
import os

def read_todos(todos_loc='./PythonPerDayPractice/App1-ToDoApp/todos.txt'):
    '''
    functions will be reading todos file
    todos_loc : type <str>
    '''
    with open(todos_loc,"r") as file1:
        todos = file1.readlines()
    return todos


def write_todos(txt, todos_loc='./PythonPerDayPractice/App1-ToDoApp/todos.txt'):
    '''
    functions will be writing todos in todo.txt file
    todos_loc : type <str>
    '''
    with open(todos_loc,"w") as file1:
        file1.writelines(txt)


def make_archive(filepaths, dest_dir):
    '''
    It helps in compressing the selected files into a folder
    '''
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


def extract_archive(archivepath, dest_dir):
    '''
    It helps in extracting all the files present in a compressed folder
    '''
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


def send_email(message):

    host = "smtp.gmail.com"
    port = 465

    # Procedure to set env variables: 
    # Go to System Properties -> Environment Variables -> Add env variables in User Variables
    username = os.getenv("RECEIVER-EMAIL")
    password = os.getenv("GOOGLE-EMAIL-PASSWORD")

    receiver = os.getenv("RECEIVER-EMAIL")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(user=username, password=password)
        server.sendmail(username, receiver, message)







if __name__ == "__main__":
    print(read_todos())
    print("utilities.py specific print commands won't run in wrapper main script")


