import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("data.txt"):
    with open("data.txt", "w"):
        pass

sg.theme("DarkPurple4")

clock = sg.Text(key="clock")
label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(key="Add", tooltip="add an item", image_source="add.png",
                       mouseover_colors="LightBlue2", size=2)

edit_button = sg.Button("Edit")
listbox = sg.Listbox(values=functions.get_todos(), size=(45, 10),
                     enable_events=True, key="todos")

complete_button = sg.Button(key="Complete", tooltip="complete", image_source="complete.png",
                            mouseover_colors="LightBlue2", size=3)
exit_button = sg.Button("Exit")

window = sg.Window("My to-do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [listbox, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 13))
while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d , %Y %H %M %S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value='')
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)

                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("please, select an item first")
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("please, select an item first")
        case "Exit":
            break
        case "todos":
            window["todo"].update(value=values["todos"][0])

        case sg.WIN_CLOSED:
            break

