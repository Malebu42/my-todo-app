import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo App.")
st.write("This app tracks ur todos")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    try:
        if checkbox:
            todos.pop(index)
            functions.write_todos(todos)
            del st.session_state[todo]
            st.experimental_rerun()
    except TypeError:
        print("Type Error")

st.text_input(label="", placeholder ="Add new todo",
              on_change=add_todo, key = 'new_todo')

st.session_state