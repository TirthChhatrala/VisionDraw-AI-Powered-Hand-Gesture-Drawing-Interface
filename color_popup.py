from tkinter import Tk, colorchooser

def choose_color():
    try:
        root = Tk()
        root.withdraw()
        color = colorchooser.askcolor(title="Choose Drawing Color")
        root.destroy()
        if color[0]:
            return tuple(map(int, color[0]))[::-1]  # RGB to BGR
    except:
        return None
