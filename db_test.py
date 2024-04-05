import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

id = cur.execute("SELECT ID FROM Prompts").fetchall()
created = cur.execute("SELECT Created FROM Prompts").fetchall()
ingredients = cur.execute("SELECT IngredientList FROM Prompts").fetchall()
msg = cur.execute("SELECT msg FROM Prompts").fetchall()

i = 0;

while i < len(id):
    print(i)
    print("ID: " + str(id[i]) + ", Time: " + str(created[i]) + ", Ingredients: " + str(ingredients[i]))
    print("Recipe: " + str(msg[i]))

    i += 1

connection.commit()
connection.close()