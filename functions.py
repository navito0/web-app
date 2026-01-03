import zipfile
import pathlib

def get_todos(filepath="todos.txt"):
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todo_action,filepath="todos.txt"):
    with open(filepath, "w") as file:
        file.writelines(todo_action)

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir,"compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        for filepath in filepaths:
            archive.write(filepath)

print(__name__)
if __name__ == "__main__":
    make_archive(filepaths=["todos.txt"], dest_dir="dest")