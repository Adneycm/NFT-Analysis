import sqlite3
from dataclasses import dataclass

class Database:
    
    def __init__(self, databaseName):
        self.databaseName = databaseName
        self.conn = sqlite3.connect(databaseName + ".db")
        self.c = self.conn.cursor()
        self.c.execute("""CREATE TABLE IF NOT EXISTS note (
                            id INTEGER PRIMARY KEY,
                            title TEXT,
                            content TEXT NOT NULL
                            )""")

    # Métodos
 

    def get_all(self):
        listLines = self.c.execute("""SELECT id, title, content FROM note""")
        notes = []
        for linha in listLines:
            notes.append(Note(linha[0], linha[1], linha[2]))
        return notes
