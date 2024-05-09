from flask import Flask, render_template
import pandas as pd

loc = 'e:\\Job & Interview Kit\\Revision Material\\DS & Algos - Python & JavaScript\\PythonPractise2024\\PythonPerDayPractice\\App9-TheasurasAPI'

# theasuras app

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/theasuras/api/<word>")
def eng_dict(word):

    # load data only when this specific endpoint is called
    df = pd.read_csv(f'{loc}\\data\\dictionary.csv')
    df['word'] = df['word'].apply(lambda x: str(x).lower())
    df['definition'] = df['definition'].apply(lambda x: str(x).lower())

    word = str(word)    
    definition = df[df['word'] == word]['definition'].squeeze()

    return {
        "word": word,
        "definition": definition
    }

if __name__ == "__main__":
    app.run(debug=True, port=5002)