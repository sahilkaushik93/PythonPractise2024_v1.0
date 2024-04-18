file1 = open('./PythonPerDayPractice/App1-ToDoApp/todos.txt',"w")
todos1 = file1.writelines(["task1\n","task2\n","task3\n"])
file1.close()

file2 = open('./PythonPerDayPractice/App1-ToDoApp/todos.txt',"r")
todos2 = file2.readlines()
print(todos2)
file2.close()