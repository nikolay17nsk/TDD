import sqlite3

def vh(a, b, c):
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS stocks
                   (token text, api text, language text)''')
    sss = (a, b, c)
    cursor.execute("insert into stocks values (?, ?, ?)", sss)
    conn.commit()

def otvet():
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stocks")
    zap = cursor.fetchall()
    conn.commit()
    return zap

def exit_1():
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute('''DROP TABLE IF EXISTS stocks''')
    conn.commit()
    
