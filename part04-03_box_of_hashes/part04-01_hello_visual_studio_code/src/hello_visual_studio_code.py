editor=""
while editor!="visual studio code":
    editor=input("Editor:")
    editor=editor.lower()
    if editor=="notepad" or editor=="word":
        print("awful")
    elif editor=="visual studio code":
        print("an excellent choice!")
    else:
        print("not good")

