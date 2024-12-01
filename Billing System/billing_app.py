from tkinter import *
from tkinter import messagebox

if __name__ == '__main__':
    root = Tk()
    Width = 960
    Height = 540
    root.geometry(f"{Width}x{Height}")
    root.minsize(480, 270)
    root.maxsize(1920, 1080)
    root.title("Billing Software")
    root.iconbitmap("logo.ico")
    
    # Configure root grid layout to expand
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    
    main_frame = Frame(root, bg="light blue", borderwidth=5, relief=GROOVE)
    main_frame.grid(padx=10, pady=10, sticky=NSEW)

    # Configure rows and columns for main_frame to allow expansion
    main_frame.grid_rowconfigure(0, weight=1)  # Allow row 0 to expand
    main_frame.grid_columnconfigure(0, weight=1)  # Allow column 0 to expand

    first_frame = Frame(main_frame, bg="blue", borderwidth=5, relief=GROOVE)
    first_frame.grid(row=0, column=0, padx=5, pady=5, sticky=EW)

    # Configure row and column inside first_frame to allow expansion
    first_frame.grid_rowconfigure(0, weight=1)  # Row 0 will expand in first_frame
    first_frame.grid_columnconfigure(0, weight=1)  # Column 0 will expand in first_frame

    # Label inside first_frame
    Label(first_frame, text="Billing Software", bg="pink", font=("Times New Roman", 24, "bold"), borderwidth=5, relief=GROOVE).grid( sticky=EW)
    
    second_frame = Frame(main_frame, bg="blue", borderwidth=5, relief=GROOVE)
    second_frame.grid(row=1, column=0, padx=5, pady=5, sticky=EW)

    second_frame.grid_rowconfigure(0, weight=1)  
    second_frame.grid_columnconfigure(0, weight=1) 





    # Run the main loop
    root.mainloop()
