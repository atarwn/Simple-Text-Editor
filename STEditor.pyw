import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox

def set_syntax(new_syntax):
    syntax.set(new_syntax)

def open_file(text_area):
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text_area.delete('1.0', tk.END)
            text_area.insert('1.0', content)

def save_file(text_area):
    file_path = filedialog.asksaveasfilename(defaultextension=f".{syntax.get()}")
    if file_path:
        with open(file_path, 'w') as file:
            content = text_area.get('1.0', tk.END)
            file.write(content)

def show_about():
    messagebox.showinfo("О программе", "Простой текстовый редактор\nВерсия 1.0\nРазработчик: atarwn")


root = tk.Tk()
root.title("Простой текстовый редактор")
root.geometry('300x200')

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
text_area.pack(expand=True, fill='both')

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Открыть", command=lambda: open_file(text_area))
file_menu.add_command(label="Сохранить", command=lambda: save_file(text_area))
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.quit)

syntax_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Синтаксис", menu=syntax_menu)
syntax_menu.add_radiobutton(label="Текст", command=lambda: set_syntax("txt"))
syntax_menu.add_radiobutton(label="HTML", command=lambda: set_syntax("html"))
syntax_menu.add_radiobutton(label="CSS", command=lambda: set_syntax("css"))
syntax_menu.add_radiobutton(label="JS", command=lambda: set_syntax("js"))
syntax_menu.add_separator()
syntax_menu.add_radiobutton(label="Python", command=lambda: set_syntax("py"))
syntax_menu.add_radiobutton(label="Lua", command=lambda: set_syntax("lua"))

help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Справка", menu=help_menu)
help_menu.add_command(label="О программе", command=show_about)

syntax = tk.StringVar(value="txt")
syntax.set("txt")

root.mainloop()