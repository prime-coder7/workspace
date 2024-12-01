from tkinter import *

if __name__ == '__main__':
    root = Tk()
    root.geometry("600x400")

    # Create the main frame with a border
    frame = Frame(root, borderwidth=5, relief=SOLID, bg="light blue")
    frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=300, height=200)

    # Place label inside the frame
    label = Label(frame, text="Billing Software", fg="black", bg="pink", font=("Arial", 14))
    label.place(relx=0.5, rely=0.5, anchor=CENTER)  # Center the label inside the frame

    # Add a label on the top border of the frame (near the border)
    top_border_label = Label(frame, text="Top Border", fg="black", bg="yellow", font=("Arial", 10))
    top_border_label.place(relx=0.5, y=5, anchor=N)  # Place near the top border

    # Add a label on the bottom border of the frame (near the border)
    bottom_border_label = Label(frame, text="Bottom Border", fg="black", bg="green", font=("Arial", 10))
    bottom_border_label.place(relx=0.5, rely=1.0, anchor=S, y=-5)  # Place near the bottom border

    # Add a label on the left border of the frame (near the border)
    left_border_label = Label(frame, text="Left Border", fg="black", bg="purple", font=("Arial", 10))
    left_border_label.place(x=5, rely=0.5, anchor=W)  # Place near the left border

    # Add a label on the right border of the frame (near the border)
    right_border_label = Label(frame, text="Right Border", fg="black", bg="orange", font=("Arial", 10))
    right_border_label.place(x=295, rely=0.5, anchor=E)  # Place near the right border

    root.mainloop()
