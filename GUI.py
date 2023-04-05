import functions
import PySimpleGUI as sg


label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(button_text="Add")

edit_button = sg.Button("Edit")
listbox = sg.Listbox(values=functions.get_todos(), size=[45, 10],
                     enable_events=True,key="todos")

window = sg.Window("My to-do App",
                   layout=[[label], [input_box, add_button], [listbox, edit_button]],
                   font=("Helvetica", 13))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values["todos"])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            print("todo_to_edit =", todo_to_edit)
            new_todo = values["todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)

            window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=values["todos"][0])

        case sg.WIN_CLOSED:
            break

window.close()
