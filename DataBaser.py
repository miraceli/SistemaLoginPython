import sqlite3 

conn = sqlite3.connect('dogtrack.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    mail TEXT NOT NULL,
    user TEXT NOT NULL,
    pass TEXT NOT NULL
);
""")

# exemplo de inserção
# cursor.execute("""
# INSERT INTO Users(name, mail, user, pass) VALUES ()
# );
# """)

print ("Conectado ao banco de dados com sucesso!")

