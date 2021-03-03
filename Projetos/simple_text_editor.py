from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile, asksaveasfilename

def openfile():
    blank.delete("1.0", END)
    file = askopenfile(mode="R", filetypes=[("text files", "*.txt")])
    if file is not None:
        text = file.read()
        blank.insert("1.0", text)

def savefile():
    text = blank.get("1.0", "end-1c")
    file = asksaveasfilename(title="Save", filetypes=[("text files", "*.txt")])
    with open(file,"w") as data:
        data.write(text)

window = Tk()
window.title("Text Editor")

menubar = Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=savefile)
filemenu.add_command(label="Exit", command=window.destroy)

blank = Text(window, font=("arial", 10))
blank.pack()

if __name__ == "__main__":
    window.mainloop()
