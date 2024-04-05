import os, sqlite3
 
from flask import Flask, redirect, render_template, request, url_for
from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get(".env"),
)

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
 
@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        ingredient_list = request.form["IngredientList"]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.6,
            messages=[
                {"role": "system","content": "A user will provide you with a comma seperated list of ingredients.\
                Using those ingredients create a recipe that includes at least fifty percent of the ingredients provide by the user."},
                {"role": "user", "content": ingredient_list}
            ]
        )

        msg = response.choices[0].message.content
        
        conn = get_db_connection()
        conn.execute("INSERT INTO Prompts (IngredientList, Msg) VALUES (?,?)",
                     (ingredient_list, msg))
        conn.commit()
        conn.close()
        return redirect(url_for("index", result=msg))

    result = request.args.get("result") 
    return render_template("index.html", result=result)