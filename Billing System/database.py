import sqlite3

def create_connection():
    conn = sqlite3.connect('bills.db')
    return conn
    
def create_bills_table():
    conn = create_connection()
    query = conn.cursor()
    
    query.execute('''
                  CREATE TABLE IF NOT EXIST bills
                  (bill_no INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, phone_no INTEGER, total REAL)''')
    conn.commit()
    conn.close()
                  
def add_bill(n, p, t):
    name = n
    phone_no = p
    total = t
    
    conn = create_connection()
    query = conn.cursor()
    query.execute("INSERT INTO users (name, phone_no, total) values (?, ?)", (name, phone_no, total))
    conn.commit()
    conn.close()

import sqlite3

# Function to get the latest Bill No. from the database
def get_latest_bill_no():
    conn = create_connection()
    query = conn.cursor()
    
    # Query to get the latest Bill No.
    query.execute("SELECT MAX(bill_no) FROM bills")
    result = query.fetchone()
    
    try:
        # If no bill is found, return 0
        if result[0] is None:
            return 1
        else:
            return result[0] + 1  # Increment the latest Bill No. by 1 for the next bill
    finally:
        conn.close()

    