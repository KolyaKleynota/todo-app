import functions
import PySimpleGUI as sg


label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo")

window = sg.Window("My to-do App", layout=[[label, input_box]])
window.read()
window.close()