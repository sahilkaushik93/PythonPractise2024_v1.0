import streamlit as st
import pandas as pd

loc = "E:\Job & Interview Kit\Revision Material\DS & Algos - Python & JavaScript\PythonPractise2024\PythonPerDayPractice\App2-ProjectShowcaseApp"

# reading data.csv:
data = pd.read_csv(f"{loc}\data.csv", sep=";")

# setting up page layout width
st.set_page_config(layout="wide")

# ".columns" method will return two column objects
col1, col2 = st.columns(2)

# adding image and introduction
with col1:
    st.image(f"{loc}\images\profile_photo.png")

with col2:
    st.title("Sahil Kaushik")
    
    content1 = """
    Highly skilled professional with hands-on knowledge on multiple tech stacks like Clouds (AWS, Azure, GCP), 
    Machine Learning Development and with a proven track record of successfully implementing end-to-end ML 
    solutions & AI automated solutions. Proficient in Python & R programming and AWS services. Strong 
    analytical and problem-solving abilities, coupled with excellent communication skills.
    """
    st.info(content1)

    
    st.write("Location: India")
    st.write("Skills: Artificial Intelligence, Data Science, Python, R.")
    st.write("Total years of Experience: 6 years")
    st.write("LinkedIn: www.linkedin.com/in/sahilkaushik1412")
    st.write("GitHub: https://github.com/sahilkaushik93")
    
# adding indicators
content2 = """
Below you can find some of the apps I have built. Feel free to contact me!
"""
st.info(content2)

# adding all apps information
col3, col4 = st.columns(2)

# st.divider()
with col3:
    for index, value in data[:int(len(data)/2)].iterrows():
    # print(index, ":", value["title"])
        # st.divider()
        st.header(value["title"])
        st.write(value["description"])
        st.image(f"{loc}\images\{value['image']}")
        st.write(f"[GitHub Code]({value['url']})")
        # st.divider()

# st.divider()
with col4:
    for index, value in data[int(len(data)/2):].iterrows():
        # st.divider()
        st.header(value["title"])
        st.write(value["description"])
        st.image(f"{loc}\images\{value['image']}")
        st.write(f"[GitHub Code]({value['url']})")
        # st.divider()















