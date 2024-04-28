## Import Libraries
# sys to access "utilities.py" present in some other folder structure
# "utilities" to access all supporting utility functions
# "streamlit" for creating streamlit app
import sys
sys.path.append('E:\Job & Interview Kit\Revision Material\DS & Algos - Python & JavaScript\PythonPractise2024\PythonPerDayPractice')
import utilities
import streamlit as st
import time

# Making web page adjusted w.r.t APP size
st.set_page_config(layout="wide")

# current time
now = time.strftime("%b %d, %Y %H:%M:%S")

# reading todos
todos = utilities.read_todos()

# appending todo task
def add_todo():
    # st.session_state is a dict with structure:
    # {"key provided in st.text_input": "value provided in web app by user"}
    todo = st.session_state["new_todo"]
    print("todo: ",todo)
    todos.append(f"\n{now} : {todo}")
    utilities.write_todos(todos)

# Title
st.title("To Do App !!")
st.subheader("This is my to do app.")
st.write("This app is to increase your productivity by tracking your daily activity.")

# Checkbox
# st.checkbox("Work on python skills.")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{todo}")
    if checkbox:
        todos.pop(index)
        utilities.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

# Input Textbox
st.text_input(label="Enter your task here:", 
              placeholder="Add new todo....",
              on_change=add_todo,
              key="new_todo")

# session_state is a dict containing widget information
# All the widgets that contains a "key" defined will appear in it
print("st.session_state:-", st.session_state)