from tkinter import *
from tkinter import filedialog

class Notepad(Tk):
    def __init__(self, name):
        super().__init__()
        if name == '':
            self.filename = 'Untitled.txt'
        else:
            self.filename = name
        self.title('NotNotepad - ' + self.filename)
        self.resizable(True, True)
        menubar = Menu(self)
        cascade_menu_file = Menu(menubar, tearoff=0)
        cascade_menu_file.add_command(label="Save", command=self.save) 
        cascade_menu_file.add_command(label="Save As", command=self.save_file_as)
        cascade_menu_file.add_command(label="Open", command=self.open_file)
        cascade_menu_edit = Menu(menubar, tearoff=0)
        cascade_menu_edit.add_command(label="Zoom", command=self.zoom)
        menubar.add_cascade(label='File', menu=cascade_menu_file)
        menubar.add_cascade(label='Edit', menu=cascade_menu_edit)
        self.config(menu=menubar)
        self.font_size = 12
        scroll = Scrollbar(self)
        scroll.pack(side=RIGHT, fill=Y)
        self.textbox = Text(self, yscrollcommand=scroll.set)
        self.textbox.pack(fill=BOTH, expand=1)
        self.bind('<Control-s>', self.save_shortcut)
        self.bind('<Control-S>', self.save_file_as_shortcut)
        self.bind('<Control-KP_Add>', self.zoom_shortcut)
        if name != '':
            with open(name, 'r+') as file:            
                text = file.readline()
                self.textbox.insert("1.0", text)
    
    def save_file_as(self):
        saved_file = filedialog.asksaveasfile(initialfile='Untitled.txt', filetypes=[('Text Document', '*.txt')])
        with open(saved_file.name, "w") as file:
            file.write(self.textbox.get("1.0", END))

    def save_file_as_shortcut(self, event):
        saved_file = filedialog.asksaveasfile(initialfile='Untitled.txt', filetypes=[('Text Document', '*.txt')])
        with open(saved_file.name, "w") as file:
            file.write(self.textbox.get("1.0", END))

    def open_file(self):
        self.textbox.delete('1.0', END)
        opened_file = filedialog.askopenfilename(filetypes=[('Text Document', '*.txt')])
        new_app = Notepad(opened_file)
        self.destroy()

    def save(self):
        with open(self.filename, ('w')) as file:
            file.write(self.textbox.get("1.0", END))

    def save_shortcut(self, event):
        with open(self.filename, ('w')) as file:
            file.write(self.textbox.get("1.0", END))

    def zoom(self):
        self.font_size +=10
        self.textbox.configure(font=self.font_size)
        new = self.textbox.get("1.0", END)
        self.textbox.delete("1.0", END)
        self.textbox.insert("1.0", new)
# why does this shit only work once?
    def zoom_shortcut(self, event):
        self.font_size +=10
        self.textbox.configure(font=self.font_size)
        new = self.textbox.get("1.0", END)
        self.textbox.delete("1.0", END)
        self.textbox.insert("1.0", new)

if __name__ == '__main__':
    app = Notepad('')
    app.mainloop()
