import tkinter as tk
from tkinter import messagebox
import os

class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")
        self.root.geometry("900x500+300+200")
        self.file_paths = [f"text_file_{i}.txt" for i in range(1, 7)]
        self.create_buttons()

    def create_buttons(self):
        # ساخت کلید بدون استفاده از حلفه
        self.create_button("کار خانگی مثال تابع", self.file_paths[0])
        self.create_button("سلسله فیبوناچی", self.file_paths[1])
        self.create_button(" مثال فکتوریل", self.file_paths[2])
        self.create_button("Tkinter code", self.file_paths[3])


    def create_button(self, text, file_path):
        button = tk.Button(self.root, text=text, background="yellow",font=30, command=lambda p=file_path: self.open_text_editor(p))
        button.pack(padx=10, pady=10, expand=True)

    def open_text_editor(self, file_path):
        editor_window = tk.Toplevel(self.root)
        editor_window.title(f"Edit Text - {file_path}")
        editor_window.geometry("900x500+300+200")
        
        # Create a frame to hold the text area and scrollbar
        frame = tk.Frame(editor_window)
        frame.pack(expand=1, fill=tk.BOTH)
        
        # Create the text area with scrollbar
        text_area = tk.Text(frame, wrap=tk.WORD, font=("Arial", 12))
        text_area.pack(side=tk.LEFT, expand=1, fill=tk.BOTH)
        
        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=text_area.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        text_area.config(yscrollcommand=scrollbar.set)
        
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    text_area.insert(tk.END, file.read())
            except Exception as e:
                messagebox.showerror("File Error", f"Error reading file: {e}")

        save_button = tk.Button(editor_window, text="Save", background="red", command=lambda: self.save_text(file_path, text_area))
        save_button.pack(pady=10, expand=True, fill="both")

    def save_text(self, file_path, text_area):
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(text_area.get("1.0", tk.END).strip())
            messagebox.showinfo("Save File", "File saved successfully!")
        except Exception as e:
            messagebox.showerror("File Error", f"Error saving file: {e}")

def main():
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
 
a = 0
for count in range(a):
    a = (count+ 1)
    count+= 1
print()    
































































# from Tkinter import * # Frame, Tk, BOTH, Text, Menu, END
# import tkFileDialog 

# class Example(Frame):

#     def __init__(self, parent):
#         Frame.__init__(self, parent)   

#         self.parent = parent        
#         self.initUI()

#     def initUI(self):

#         self.parent.title("File dialog")
#         self.pack(fill=BOTH, expand=1)

#         menubar = Menu(self.parent)
#         self.parent.config(menu=menubar)

#         fileMenu = Menu(menubar)
#         fileMenu.add_command(label="Open", command=self.onOpen)
#         menubar.add_cascade(label="File", menu=fileMenu)        

#         self.txt = Text(self)
#         self.txt.pack(fill=BOTH, expand=1)


#     def onOpen(self):

#         ftypes = [('Python files', '*.py'), ('All files', '*')]
#         dlg = tkFileDialog.Open(self, filetypes = ftypes)
#         fl = dlg.show()

#         if fl != '':
#             text = self.readFile(fl)
#             self.txt.insert(END, text)

#     def readFile(self, filename):

#         f = open(filename, "r")
#         text = f.read()
#         return text


# def main():

#     root = Tk()
#     ex = Example(root)
#     root.geometry("300x250+300+300")
#     root.mainloop()  


# if __name__ == '__main__':
#     main()