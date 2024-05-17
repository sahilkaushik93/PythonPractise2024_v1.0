# Import packages
import streamlit as st
import plotly.express as px
from Dashboard_Backend import get_data

# root dir 
loc = "E:\Job & Interview Kit\Revision Material\DS & Algos - Python & JavaScript\PythonPractise2024\PythonPerDayPractice\App8-HistoricalWeatherAPI"

# Add title, text input, slider, selectbox and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

# def get_data(days):
#     dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
#     temperatures = [10, 11, 15]
#     temperatures = [days*i for i in temperatures]
#     return dates, temperatures

if place:
     # Get the temperature/sky data
    filtered_data = get_data(place=place, forecast_days=days)

    if filtered_data is not None:
        # Create a temperature plot
        if option == "Temperature":
            
            temperatures = [dict["main"]["temp"]/10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]

            figure = px.line(x=dates, y=temperatures, labels={"x":"Date", "y":"Temperature (C)"})
            st.plotly_chart(figure)
        else:
            images = {"Clear": f"{loc}/images/clear.png", "Clouds": f"{loc}/images/cloud.png",
                    "Rain": f"{loc}/images/rain.png", "Snow": f"{loc}/images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)
    else:
        st.text("Oops! You entered a non existing place.")
else:
    st.text("Oops! You entered a non existing place.")