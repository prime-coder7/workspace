import os
from tkinter import *
from tkinter import messagebox, simpledialog, font as tkFont
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Function to handle loading the image icon
def load_icon(icon_path):
    try:
        # Try to set the icon from the provided path
        root.iconbitmap(icon_path)
    except Exception as e:
        print(f"Error loading icon: {e}")
        # Fallback icon if the provided path fails
        fallback_icon = "fallback.ico"  # Make sure this fallback icon is included in the project
        if os.path.exists(fallback_icon):
            root.iconbitmap(fallback_icon)
        else:
            print("Fallback icon also missing!")

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file:
        with open(file, 'r') as f:
            TextArea.delete(1.0, END)
            TextArea.insert(INSERT, f.read())
        root.title(f"{os.path.basename(file)} - Notepad")

def saveFile():
    global file
    if file is None:
        file = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file:
        with open(file, 'w') as f:
            content = TextArea.get(1.0, END).strip()  # Strip removes leading/trailing whitespace
            f.write(content)
        root.title(f"{os.path.basename(file)} - Notepad")

def saveAs():
    global file
    file = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file:
        with open(file, 'w') as f:
            content = TextArea.get(1.0, END).strip()  # Strip removes leading/trailing whitespace
            f.write(content)
        root.title(f"{os.path.basename(file)} - Notepad")

def exit():
    if TextArea.get(1.0, END) != "\n":
        response = messagebox.askyesnocancel("Quit", "Do you want to save changes?")
        if response:
            saveFile()
            root.destroy()
        elif response is False:
            root.destroy()
    else:
        root.destroy()

def undo():
    TextArea.edit_undo()

def redo():
    TextArea.edit_redo()

def cut():
    TextArea.event_generate("<<Cut>>")

def copy():
    TextArea.event_generate("<<Copy>>")

def paste():
    TextArea.event_generate("<<Paste>>")

def find():
    def find_text():
        word = simpledialog.askstring("Find", "Enter text to find:")
        if word:
            start_pos = TextArea.search(word, "1.0", END)
            if start_pos:
                end_pos = f"{start_pos}+{len(word)}c"
                TextArea.tag_add("highlight", start_pos, end_pos)
                TextArea.mark_set("insert", end_pos)
                TextArea.see("insert")
            else:
                messagebox.showinfo("Find", "Text not found.")

    find_window = Toplevel(root)
    find_window.title("Find")
    find_window.geometry("300x100")
    find_button = Button(find_window, text="Find", command=find_text)
    find_button.pack(pady=20)

def replace():
    def replace_text():
        word_to_replace = simpledialog.askstring("Replace", "Enter text to replace:")
        replacement_word = simpledialog.askstring("Replace", "Enter replacement text:")
        content = TextArea.get(1.0, END)
        new_content = content.replace(word_to_replace, replacement_word)
        TextArea.delete(1.0, END)
        TextArea.insert(INSERT, new_content)

    replace_window = Toplevel(root)
    replace_window.title("Replace")
    replace_window.geometry("300x150")
    replace_button = Button(replace_window, text="Replace", command=replace_text)
    replace_button.pack(pady=20)

def toggle_word_wrap():
    if TextArea.cget("wrap") == "none":
        TextArea.config(wrap="word")
    else:
        TextArea.config(wrap="none")

def font():
    font_name = simpledialog.askstring("Font", "Enter font name:")
    font_size = simpledialog.askinteger("Font Size", "Enter font size:")
    if font_name and font_size:
        TextArea.config(font=(font_name, font_size))

def zoomIn():
    current_font = tkFont.Font(font=TextArea['font'])
    new_size = current_font.actual('size') + 2
    TextArea.config(font=(current_font.actual('family'), new_size))

def zoomOut():
    current_font = tkFont.Font(font=TextArea['font'])
    new_size = max(current_font.actual('size') - 2, 1)
    TextArea.config(font=(current_font.actual('family'), new_size))

def restoreDefaultZoom():
    TextArea.config(font=("lucida", 13))

def statusbar():
    status = Toplevel(root)
    status.title("Status Bar")
    status.geometry("300x100")
    label = Label(status, text="This is a simple Notepad application.")
    label.pack(pady=20)

def viewHelp():
    messagebox.showinfo("Help", "This is a simple Notepad application. Use the menu options to create, open, save, and edit text files")
    
def sendFeedback():
    feedback = simpledialog.askstring("Feedback", "Enter your feedback:")
    if feedback:
        with open("feedback.txt", "a") as f:
            f.write(feedback + "\n")
        messagebox.showinfo("Feedback", "Thank you for your feedback!")
    else:
        messagebox.showwarning("Feedback", "No feedback entered.")

def aboutNotepad():
    messagebox.showinfo("Notepad", "Notepad by Me")
    
if __name__ == "__main__":
    root = Tk()
    root.title("Untitled - Notepad")
    root.geometry("600x400")
    
    # Set the icon for the window (with error handling for missing file)
    icon_path = "F:/workspace/Notepad/notepad.ico"  # Adjust this to your icon's location
    load_icon(icon_path)
    
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand=TRUE, fill=BOTH)
    
    scrollx = Scrollbar(TextArea, orient=HORIZONTAL)
    scrollx.pack(side=BOTTOM, fill=X)
    scrollx.config(command=TextArea.xview)
    TextArea.config(xscrollcommand=scrollx.set)
    
    scrolly = Scrollbar(TextArea)
    scrolly.pack(side=RIGHT, fill=Y)
    scrolly.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scrolly.set)
    
    # Createing a Menu Bar
    menubar = Menu(root)
    
    # File Menu: Start
    file_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    
    file_menu.add_command(label="New File", command=newFile)
    file_menu.add_command(label="Open", command=openFile)
    file_menu.add_command(label="Save", command=saveFile)
    file_menu.add_command(label="Save As", command=saveAs)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=exit)
    
    root.configure(menu=menubar)
    # File Menu: End
    
    # Edit Menu: Start
    edit_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Edit", menu=edit_menu)
    
    edit_menu.add_command(label="Undo", command=undo)
    edit_menu.add_command(label="Redo", command=redo)
    edit_menu.add_separator()
    edit_menu.add_command(label="Cut", command=cut)
    edit_menu.add_command(label="Copy", command=copy)
    edit_menu.add_command(label="Paste", command=paste)
    edit_menu.add_separator()
    edit_menu.add_command(label="Find", command=find)
    edit_menu.add_command(label="Replace", command=replace)
    
    root.configure(menu=menubar)
    # Edit Menu: End
    
    # Format Menu: Start
    format_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Format", menu=format_menu)
    
    format_menu.add_command(label="Word Wrap", command=toggle_word_wrap)
    format_menu.add_command(label="Font", command=font)
    
    root.configure(menu=menubar)    
    # Format Menu: End
    
    # View Menu: Start
    view_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="View", menu=view_menu)
    
    zoom_menu = Menu(view_menu, tearoff=0)
    view_menu.add_cascade(label="Zoom", menu=zoom_menu)

    zoom_menu.add_command(label="Zoom In", command=zoomIn)
    zoom_menu.add_command(label="Zoom Out", command=zoomOut)
    zoom_menu.add_command(label="Restore Default Zoom", command=restoreDefaultZoom)
    
    view_menu.add_command(label="Status Bar", command=statusbar)
    
    root.configure(menu=menubar)    
    # View Menu: End
    
    # Help Menu: Start
    help_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help_menu)
    
    help_menu.add_command(label="View Help", command=viewHelp)
    help_menu.add_command(label="Send Feedback", command=sendFeedback)
    help_menu.add_separator()
    help_menu.add_command(label="About Notepad", command=aboutNotepad)
    
    root.configure(menu=menubar)    
    # Help Menu: End
    
    root.mainloop()
