from flask import Flask, render_template
import os

print(os.getcwd())

loc = "E:\Job & Interview Kit\Revision Material\DS & Algos - Python & JavaScript\PythonPractise2024\PythonPerDayPractice\App8-HistoricalWeatherAPI"

# creating a website object with Flask
app = Flask("Website", template_folder=f"{loc}\\templates")

# variable giving inside about.html
variable = "tutorial"

# decorator connects app method with home function i.e. 
# "/home" url connected with "tutorial.html"
@app.route("/home")
def home():
    return render_template(f"tutorial.html")

@app.route("/about/")
def about():
    return render_template(f"about.html", data = variable)

# debug = True will give you a feature of displaying errors on webpage
app.run(debug=True)