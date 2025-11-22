import sqlite3

connection = sqlite3.connect('feedbacks.db')
cursor = connection.cursor()

cmd = """
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT NOT NULL,
        usn varchar(10) NOT NULL,
        contact number(10) NOT NULL,
        email TEXT NOT NULL,
        message TEXT NOT NULL
    );
"""

cursor.execute(cmd)
connection.commit()

cmd = """
    INSERT INTO feedback (fullname, usn, contact, email, message)
    VALUES (?, ?, ?, ?, ?);
"""
'''cursor.execute(cmd, ('Mithul Byndoor', '4MW23AD021', '9108864556',
               'mithul.23ad021@sode-edu.in', 'Great course!'))
connection.commit()'''

cursor.execute(cmd, ('Shreyas Acharya', '4MW23AD047', '9101234567',
               'shreyas.23ad047@sode-edu.in', 'I am a handsome boy!'))

connection.commit()


f = cursor.execute("SELECT * FROM feedback;").fetchall()
print(f)

connection.close()
