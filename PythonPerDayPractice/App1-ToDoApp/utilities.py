# utility functions
def read_todos(todos_loc):
    '''
    functions will be reading todos file
    todos_loc : type <str>
    '''
    with open(todos_loc,"r") as file1:
        todos = file1.readlines()
    file1.close()
    return todos



if __name__ == "__main__":
    print("utilities specific print commands won't run in wrapper main script")                                                                                                               