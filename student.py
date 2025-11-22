import sqlite3

connection = sqlite3.connect('student.db')
cursor = connection.cursor()

cmd = """
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        usn varchar(10) NOT NULL,
        semester INTEGER NOT NULL,
        gender TEXT NOT NULL,
        cgpa float NOT NULL
    );
"""

cursor.execute(cmd)
connection.commit()

cmd = """
    INSERT INTO feedback (name, usn, semester, gender, cgpa)
    VALUES (?, ?, ?, ?, ?);
"""

cursor.execute(cmd, ('Mithul Byndoor', '4MW23AD021', 5, 'Male', 8.5))
connection.commit()

f = cursor.execute("SELECT * FROM feedback WHERE name = ?",('Mithul Byndoor',)).fetchall()
print(f)

connection.close()
