#function file (backend)
PATH = r"C:\Users\admin\Desktop\PYTHON APP1\sec19_webapps\todos.txt"
# when you have your files in folder in a project folder always put full file path
# if it is directly inside the project folder no need just name of file.format
# create a function that reads todos list from a file
def get_todos(filepath= PATH):         # filepath is a variable (default arguement/parameter) that has a value of constant variable
    """ Reads the todolist items from the file and
    return them to the function"""
    with open(filepath, "r") as file_local:  # opening the file to read data using with context manager way
        todos_local = file_local.readlines()  # store the data list from file to list variable todos_local
    return todos_local                  # return this variable todos_local to the function

# create a function that write my todos list to a file
def write_todos(todos_local, filepath=PATH):
    """Write the todolist items to the file"""
    with open(filepath,"w") as file_local: # opening the file to write data to it using wtih context manager way
        file_local.writelines(todos_local)
    # this function doesn't return anything so we don't put return
    # this function just writes data to file and it doesn't need to give any output


# testing the function here
if __name__ == "__main__":
    print("Hello I am a function file for todos app")
    print("I have in the list the following items:", get_todos())
    print("Function ok")

