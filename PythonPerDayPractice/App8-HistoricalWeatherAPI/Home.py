from flask import Flask, render_template
import pandas as pd

loc = "E:\Job & Interview Kit\Revision Material\DS & Algos - Python & JavaScript\PythonPractise2024\PythonPerDayPractice\App8-HistoricalWeatherAPI"

# creating a website object with Flask
# "__name__" gives a privelege in which we will get main only when current script runs if this script is 
# is imported in some other script that it will give "Home" instead of main and thus flask app won't run
app = Flask(__name__, template_folder=f"{loc}\\templates")

# reading file to be displayed at home
filename = f"{loc}\data\data_small\stations.txt"
df = pd.read_csv(filename, skiprows=17)
df = df[["STAID","STANAME                                 "]]
# print(df)

# decorator connects app method with home function i.e. 
# "/home" url connected with "tutorial.html"
@app.route("/")
def home():
    return render_template(f"home.html", data = df.to_html())

# here "<" & ">" provides a feature to take input from user dynamically
# i.e. user can provide url of api/v1 and then dynamically enter "station" & "date"
@app.route("/api/v1/<station>/<date>")
def date_specific_api_response(station, date):
    
    filename = f"{loc}\data\data\TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"]==date]['   TG'].squeeze() / 10

    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }


@app.route("/api/v1/annual/<station>/<year>")
def year_specific_api_response(station, year):
    
    filename = f"{loc}\data\data\TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"]=df["    DATE"].astype(str)
    df = df[df['    DATE'].str.startswith(str(year))]

    return df.to_dict(orient="records")

@app.route("/api/v1/<station>")
def station_specific_api_response(station):
    
    filename = f"{loc}\data\data\TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])

    return df.to_dict(orient="records")

# debug = True will give you a feature of displaying errors on webpage
# if __name__ = __main__ to run flask app only when "Home.py" runs 
# if you want to run multiple flask apps at once, you need to mention "port" no in app.run()
# by default all apps run at "port = 5000"
# if multiple apps are not running at once, then "port" variable is not required
if __name__ == "__main__":
    app.run(debug=True, port=5001)

