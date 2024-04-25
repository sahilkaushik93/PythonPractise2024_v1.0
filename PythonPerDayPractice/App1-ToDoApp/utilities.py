# utility functions
def read_todos(todos_loc='./PythonPerDayPractice/App1-ToDoApp/todos.txt'):
    '''
    functions will be reading todos file
    todos_loc : type <str>
    '''
    with open(todos_loc,"r") as file1:
        todos = file1.readlines()
    file1.close()
    return todos

def write_todos(txt, todos_loc='./PythonPerDayPractice/App1-ToDoApp/todos.txt'):
    '''
    functions will be writing todos in todo.txt file
    todos_loc : type <str>
    '''
    with open(todos_loc,"w") as file1:
        todos = file1.writelines(str(txt) + "\n")
    file1.close()
    return todos




if __name__ == "__main__":
    print("utilities.py specific print commands won't run in wrapper main script")                                                                                                               