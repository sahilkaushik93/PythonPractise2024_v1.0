from flask import Flask, render_template

# theasuras app

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/theasuras/api/<word>")
def eng_dict(word):

    word = str(word)
    definition = word.upper()

    return {
        "word": word,
        "definition": definition
    }

if __name__ == "__main__":
    app.run(debug=True)