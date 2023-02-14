#importing 3rd party module for web app after installing package
import streamlit as st
import funcfiletodos


# getting a todos list from todos.txt
# call the function get_todds() from funfiletodos module
# then store it in variable
todos = funcfiletodos.get_todos()
# todos.txt path is : C:\Users\admin\Desktop\PYTHON APP1\sec19_webapps\todos.txt

# Implemening add to do , this function is to add a todo element to the todos list
# can the value in the input text box then add it to todos list and display it in check box
def add_todo():
    todo = st.session_state["newtodo"] + "\n" #get value of key newtodo and break line and store it in variable
                                              #\n is to break line to prevent next added todo to be next to old one
    print(todo) # to test if we are getting the right todo we type in input text box
    todos.append(todo) # add the todo element in todos list
    funcfiletodos.write_todos(todos) # call the function to write the new todos list to file .txt

#to make my web app to fit on the width of the browser instead of fixed and to be used with mobile
st.set_page_config(layout="wide")

st.title("My To do App")
st.subheader("This is my to do app.")
st.write("This application is to increase your <b>productivity</b>",
         unsafe_allow_html=True)
#unsafe_allow_html= True , i use it when i use html tags in .write , such as <b></b> , <h2></h2>
#st.checkbox("Buy groceries.")
#st.checkbox("Throw the trash.")

# make a for loop inside todos variable (todos elements) and make each element as checkbox
# give a key for check box to implement complete action
#key should be same as variable of for loop
for index, todo in enumerate(todos):
    checked_element = st.checkbox(todo , key=todo)
    if checked_element: # if checked element is true , selected
        todos.pop(index) # remove the element from the list todos that corresponds to this index of checked element
        funcfiletodos.write_todos(todos) # write the updated todos list to the file by calling function that writes to
                                         # file
        # update on the web page
        del st.session_state[todo] # delete the element that has key todo from webpage
        st.experimental_rerun()    # to update/refresh the checkbox on webpage after deleting an element



# create an input text box
# adding on_change argument and key argument
st.text_input(label="Add a todo:", placeholder="Enter a todo..." , on_change=add_todo, key="newtodo")

# create a label for the coder
st.write("<b>Coded by: Eng. Haissam Bakri</b>",unsafe_allow_html=True)
#st.session_state
