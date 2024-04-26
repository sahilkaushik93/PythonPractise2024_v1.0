# utility functions
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
    
if __name__ == "__main__":
    print(read_todos())




if __name__ == "__main__":
    print("utilities.py specific print commands won't run in wrapper main script")                                                                                                               