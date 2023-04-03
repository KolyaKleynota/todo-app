def get_todos(filepath="data.txt"):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="data.txt"):
    with open("data.txt", "w") as file_local:
        file_local.writelines(todos_arg)

