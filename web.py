import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my first app")
st.write("Check the todo which is completed to remove from list")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",placeholder="Enter your todo",on_change=add_todo,key="new_todo")