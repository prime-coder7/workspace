import os
from tkinter import *
from tkinter import messagebox
import database as d

# Function to handle loading the image icon
def load_icon(icon_path):
    try:
        root.iconbitmap(icon_path)
    except Exception as e:
        print(f"Error loading icon: {e}")
        
def click_enter():
    d.add_bill()

def calculate_totals():
    try:
        # Get quantities from the user inputs (ensure to add validation)
        cosmetics_prices = [10, 20, 15, 12, 25]  # Example prices for Cosmetics
        grocery_prices = [50, 30, 40, 20, 25]    # Example prices for Grocery
        others_prices = [5, 7, 10, 4, 3]          # Example prices for Others
        
        total_cosmetics_value = 0
        total_grocery_value = 0
        total_others_value = 0
        
        # Calculate total for Cosmetics
        for i, price in enumerate(cosmetics_prices):
            quantity = float(cosmetic_entries[i].get() or 0)  # Get quantity or 0 if empty
            total_cosmetics_value += price * quantity
        
        # Calculate total for Grocery
        for i, price in enumerate(grocery_prices):
            quantity = float(grocery_entries[i].get() or 0)  # Get quantity or 0 if empty
            total_grocery_value += price * quantity
        
        # Calculate total for Others
        for i, price in enumerate(others_prices):
            quantity = float(others_entries[i].get() or 0)  # Get quantity or 0 if empty
            total_others_value += price * quantity
        
        # Tax calculations (simple 10% tax)
        cosmetics_tax_value = total_cosmetics_value * 0.10
        grocery_tax_value = total_grocery_value * 0.10
        others_tax_value = total_others_value * 0.10
        
        # Update the UI with totals and taxes
        total_cosmetics.config(text=f"{total_cosmetics_value:.2f}")
        cosmetics_tax.config(text=f"{cosmetics_tax_value:.2f}")
        
        total_grocery.config(text=f"{total_grocery_value:.2f}")
        grocery_tax.config(text=f"{grocery_tax_value:.2f}")
        
        others_total.config(text=f"{total_others_value:.2f}")
        others_tax.config(text=f"{others_tax_value:.2f}")
        
        # Calculate and display overall total
        overall_total = total_cosmetics_value + total_grocery_value + total_others_value
        overall_tax = cosmetics_tax_value + grocery_tax_value + others_tax_value
        total_amount.config(text=f"{overall_total + overall_tax:.2f}")
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for quantities.")


if __name__ == '__main__':
    root = Tk()
    Width = 1150
    Height = 650  # 16:9 Ratio
    root.geometry(f"{Width}x{Height}")
    root.minsize(1150, 650)
    # root.maxsize(1250, 680)
    root.maxsize(1920, 1080)
    root.title("Billing Software")
    icon_path = "Tkinter_assesment/Billing System/logo.ico"
    load_icon(icon_path)

    # Root Grid Configuration for dynamic resizing
    root.grid_rowconfigure(0, weight=1)  # Header
    root.grid_rowconfigure(1, weight=1)  # Customer Details
    root.grid_rowconfigure(2, weight=3)  # Items Section
    root.grid_rowconfigure(3, weight=1)  # Buttons Section
    root.grid_columnconfigure(0, weight=1)


# 1. Header Frames (1st)
    first_frame = Frame(root, bg="#074463", borderwidth=5, relief=GROOVE, pady=2)
    first_frame.grid(row=0, column=0, sticky="nsew")
    Label(first_frame, text="Billing Software", font=("Times New Roman", 24, "bold"), borderwidth=5, 
          relief=FLAT, bg="#074463", fg="white").pack(fill=X, pady=2)


# 2.Information Frames (2nd)
    customer_name_var = StringVar()
    phone_no_var = StringVar()
    
    latest_bill_no = d.get_latest_bill_no()
        
    second_frame = Frame(root, bd=5, relief=GROOVE, bg="#074463")
    second_frame.grid(row=1, column=0, sticky="nsew")
   
    second_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

    # Heading inside Information Frame
    heading = Label(second_frame, text="Customer Details", font=("Arial", 9), bg="#003366", fg="#FFFF00")
    heading.place(x=5, y=-9) 

    Label(second_frame, text="Customer Name: ", font=("Times New Roman", 12, "bold"), bg="#074463", fg="white").grid(row=0, column=0, padx=10, pady=15, sticky=E)
    Entry(second_frame, textvariable=customer_name_var).grid(row=0, column=1, padx=10, pady=15, sticky=W)

    Label(second_frame, text="Phone No: ", font=("Times New Roman", 12, "bold"), bg="#074463", fg="white").grid(row=0, column=2, padx=10, pady=15, sticky=E)
    Entry(second_frame, textvariable=phone_no_var).grid(row=0, column=3, padx=10, pady=15, sticky=W)

    Label(second_frame, text="Bill No: ", font=("Times New Roman", 12, "bold"), bg="#074463", fg="white").grid(row=0, column=4, padx=10, pady=15, sticky=E)
    Label(second_frame, text=latest_bill_no, font=("Times New Roman", 12, "bold"), bg="#074463", fg="white").grid(row=0, column=5, padx=0, pady=15, sticky=W)
    
    Button(second_frame, text="Enter", font=("Times New Roman", 12, "bold"), bg="#87CEEB", fg="black", bd=3, relief=RAISED, padx=20).grid(row=0, column=6, padx=50, pady=15, sticky=E)

# 3. Items Frame (3rd)
    items_frame = Frame(root, bd=5, relief=GROOVE, bg="#074463")
    items_frame.grid(row=2, column=0, sticky="nsew")
    items_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

    cosmetic_entries = []
    grocery_entries = []
    others_entries = []
    
    def create_item_column(parent, heading, items, col):
        column_frame = Frame(parent, bd=5, relief=GROOVE, bg="#074463")
        column_frame.grid(row=0, column=col, sticky="nsew", padx=5, pady=5)
        column_frame.grid_columnconfigure((0, 1), weight=1)

        Label(column_frame, text=heading, font=("helvetica", 9, "bold"), bg="#003366", fg="#FFFF00").grid(row=0, column=0, columnspan=2, sticky="ew", pady=5)
        for i, item in enumerate(items):
            Label(column_frame, text=f"{item}: ", font=("Times New Roman", 14), bg="#074463", fg="white").grid(row=i+1, column=0, sticky=W, padx=(10,10), pady=15)
            Entry(column_frame).grid(row=i+1, column=1, sticky=W, padx=(5,5), pady=15)

    create_item_column(items_frame, "Cosmetics", ["Bath Soap", "Face Cream", "Face Wash", "Hair Spray", "Body Lotion"], 0)
    create_item_column(items_frame, "Grocery", ["Rice", "Food Oil", "Daal", "Wheat", "Sugar"], 1)
    create_item_column(items_frame, "Others", ["Maza", "Coke", "Frooti", "Nimkos", "Biscuits"], 2)

    # Bill Area (3rd column)
    bill_area_frame = Frame(items_frame, bd=5, relief=GROOVE, bg="#074463")
    bill_area_frame.grid(row=0, column=3, sticky="nsew", padx=5, pady=5)

    # Bill Area Heading
    Label(bill_area_frame, text="Bill Area", font=("helvetica", 12, "bold"), bg="#003366", fg="#FFFF00").grid(row=0, column=0, sticky="ew")

    # Bill Canvas (where the bill content will be displayed)
    bill_canvas = Canvas(bill_area_frame, bg="white", bd=5, relief=GROOVE)
    bill_canvas.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    # Scrollbar for Bill Area (set up vertical scrolling)
    bill_scrollbar = Scrollbar(bill_area_frame, orient=VERTICAL, command=bill_canvas.yview)
    bill_scrollbar.grid(row=1, column=1, sticky="ns", padx=(0, 5))

    # Configure canvas to use the scrollbar
    bill_canvas.configure(yscrollcommand=bill_scrollbar.set)

    # Frame inside Canvas for Content (this is where your dynamic content will be displayed)
    bill_content_frame = Frame(bill_canvas, bg="white")
    bill_canvas.create_window((0, 0), window=bill_content_frame, anchor="nw")

    # Sample content for the bill (this can be dynamically generated)
    Label(bill_content_frame, text="Sample Bill Details:\n\nItem 1: $10\nItem 2: $15\nTotal: $25", 
        bg="white", fg="black", font=("Times New Roman", 12), anchor="w", justify=LEFT).pack()

    # Update the scroll region for the canvas to ensure that scrolling is enabled when content exceeds the visible area
    bill_content_frame.update_idletasks()
    bill_canvas.config(scrollregion=bill_canvas.bbox("all"))


    
#4. Button Frame (4th) 
    button_frames = Frame(root, bd=5, relief=GROOVE, bg="#074463", height=170)
    button_frames.grid(row=3, column=0, sticky="nsew")
    button_frames.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)

    # Heading inside Button Frame
    heading = Label(button_frames, text="Bill Menu", font=("Arial", 9), bg="#003366", fg="#FFFF00")
    heading.place(x=5, y=-9)

    Label(button_frames, text="Total Cosmetics: ", font=("Times New Roman", 12, "bold"), bg="#074463", fg="white").grid(row=0, column=0, padx=(20, 10), pady=(25, 10), sticky=W)
    total_cosmetics = Label(button_frames, text="0.00", font=("Times New Roman", 12, "bold"), bg="white", fg="black", padx=10)
    total_cosmetics.grid(row=0, column=1, padx=(0, 20), pady=(25, 10), sticky=W)

    Label(button_frames, text="Cosmetics Tax: ", font=("Times New Roman", 12, "bold"), bg="#074463", fg="white").grid(row=0, column=2, padx=(20, 10), pady=(25, 10), sticky=W)
    cosmetics_tax = Label(button_frames, text="0.00", font=("Times New Roman", 12, "bold"), bg="white", fg="black", padx=10)
    cosmetics_tax.grid(row=0, column=3, padx=(0, 20), pady=(25, 10), sticky=W)
    
    Label(button_frames, text="Total: ", font=("Times New Roman", 12, "bold"), bg="#074463", fg="white").grid(row=0, column=4, padx=(20, 10), pady=(25, 10), sticky=E)
    total_amount = Label(button_frames, text="0.00", font=("Times New Roman", 12, "bold"), bg="white", fg="black", padx=20)
    total_amount.grid(row=0, column=5, padx=(0, 20), pady=(25, 10), sticky=W)
    
    Label(button_frames, text="Total Tax: ", font=("Times New Roman", 12, "bold"), bg="#074463", fg="white").grid(row=0, column=6, padx=(20, 10), pady=(25, 10), sticky=E)
    total_tax = Label(button_frames, text="0.00", font=("Times New Roman", 12, "bold"), bg="white", fg="black", padx=20)
    total_tax.grid(row=0, column=7, padx=(0, 20), pady=(25, 10), sticky=W)

    Label(button_frames, text="Total Grocery: ", font=("Times New Roman", 12, "bold"), bg="#074463", fg="white").grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky=W)
    total_grocery = Label(button_frames, text="0.00", font=("Times New Roman", 12, "bold"), bg="white", fg="black", padx=10)
    total_grocery.grid(row=1, column=1, padx=(0, 20), pady=(10, 10), sticky=W)

    Label(button_frames, text="Grocery Tax: ", font=("Times New Roman", 12, "bold"), bg="#074463", fg="white").grid(row=1, column=2, padx=(20, 10), pady=(10, 10), sticky=W)
    grocery_tax = Label(button_frames, text="0.00", font=("Times New Roman", 12, "bold"), bg="white", fg="black", padx=10)
    grocery_tax.grid(row=1, column=3, padx=(0, 20), pady=(10, 10), sticky=W)

    Label(button_frames, text="Other's Total: ", font=("Times New Roman", 12, "bold"), bg="#074463", fg="white").grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky=W)
    others_total = Label(button_frames, text="0.00", font=("Times New Roman", 12, "bold"), bg="white", fg="black", padx=10)
    others_total.grid(row=2, column=1, padx=(0, 20), pady=(10, 10), sticky=W)

    Label(button_frames, text="Others Tax: ", font=("Times New Roman", 12, "bold"), bg="#074463", fg="white").grid(row=2, column=2, padx=(20, 10), pady=(10, 10), sticky=W)
    others_tax = Label(button_frames, text="0.00", font=("Times New Roman", 12, "bold"), bg="white", fg="black", padx=10)
    others_tax.grid(row=2, column=3, padx=(0, 20), pady=(10, 10), sticky=W)

    def generate_button(parent, txt, col, cmd):
        bg_color = "#87CEEB"  
        if txt == "Exit":
            bg_color = "#B22222"  
        
        btn = Button(parent, text=txt, command=cmd, font=("helvetica", 11, "bold"), relief=RAISED, bd=5, bg=bg_color, fg="black", padx=25, pady=5)
        btn.grid(row=1, column=col, rowspan=2, padx=20, pady=0) 

    def demo():
        pass

    # Create buttons
    total_btn = generate_button(button_frames, "Total", 4, demo)
    generate_bill_btn = generate_button(button_frames, "Generate Bill", 5, demo)
    clear_btn = generate_button(button_frames, "Clear", 6, demo)
    exit_btn = generate_button(button_frames, "Exit", 7, quit)


    root.mainloop()