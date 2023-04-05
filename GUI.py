import functions
import PySimpleGUI as sg


label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo", key="add_b")
add_button = sg.Button(button_text="Add")

window = sg.Window("My to-do App",
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 13))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["add_b"] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
