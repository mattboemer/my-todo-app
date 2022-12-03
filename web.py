import streamlit as st
import functions as funcs

todos = funcs.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    if todo != '':
        todos.append(todo.capitalize() + '\n')
        funcs.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=(index, todo))
    if checkbox:
        todos.pop(index)
        funcs.write_todos(todos)
        del st.session_state[(index, todo)]
        st.experimental_rerun()

st.text_input(label="Add new todo.", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")
