import sqlite3

database = sqlite3.connect('ls7_homework.db')
cursor = database.cursor()

cursor.execute('''
CREATE TABLE json_gazetauz(
    json_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT
    teaser TEXT
    data TEXT
);
''')

database.close()