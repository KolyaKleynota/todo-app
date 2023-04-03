from functions import get_todos, write_todos

while True:
    user_addition = input("type add , show , edit or exit: ")
    user_addition = user_addition.strip()

    if user_addition.startswith("add"):
        todo = user_addition[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_addition.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index+1}. {item}")
    elif user_addition.startswith("edit"):
        try:
            number = int(user_addition[5:])

            todos = get_todos()

            new_todo = input("Enter the new todo: ")
            todos[number-1] = new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print("Its not a number")
            continue

    elif user_addition.startswith("complete"):
        try:
            number = int(user_addition[9:])

            todos = get_todos()

            todos.pop(number-1)

            write_todos(todos)
        except ValueError:
            print("Its not a number")
            continue

    elif user_addition.startswith("exit"):
        break
    else:
        print("command is now valid")


