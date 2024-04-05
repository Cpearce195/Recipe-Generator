import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

with open('schema.sql') as f:
    script = f.read()
    cur.executescript(script)

cur.execute("INSERT INTO Prompts (IngredientList, Msg) VALUES ('Carrot, Beans, Salt', 'Here is a tasty treat')")

connection.commit()
connection.close()