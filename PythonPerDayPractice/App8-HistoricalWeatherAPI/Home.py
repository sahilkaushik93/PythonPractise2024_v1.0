from flask import Flask, render_template

loc = "E:\Job & Interview Kit\Revision Material\DS & Algos - Python & JavaScript\PythonPractise2024\PythonPerDayPractice\App8-HistoricalWeatherAPI"

# creating a website object with Flask
# "__name__" gives a privelege in which we will get main only when current script runs if this script is 
# is imported in some other script that it will give "Home" instead of main and thus flask app won't run
app = Flask(__name__, template_folder=f"{loc}\\templates")

# decorator connects app method with home function i.e. 
# "/home" url connected with "tutorial.html"
@app.route("/")
def home():
    return render_template(f"home.html")

# here "<" & ">" provides a feature to take input from user dynamically
# i.e. user can provide url of api/v1 and then dynamically enter "station" & "date"
@app.route("/api/v1/<station>/<date>")
def api_response(station, date):
    temperature = 25
    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }

# debug = True will give you a feature of displaying errors on webpage
# if __name__ = __main__ to run flask app only when "Home.py" runs 
if __name__ == "__main__":
    app.run(debug=True)

    