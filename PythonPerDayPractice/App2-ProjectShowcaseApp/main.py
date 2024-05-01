import streamlit as st

loc = "E:\Job & Interview Kit\Revision Material\DS & Algos - Python & JavaScript\PythonPractise2024\PythonPerDayPractice\App2-ProjectShowcaseApp"

# setting up page layout width
st.set_page_config(layout="wide")

# ".columns" method will return two column objects
col1, col2 = st.columns(2)

with col1:
    st.image(f"{loc}\images\profile_photo.png")

with col2:
    st.title("Sahil Kaushik")
    content = """
    Highly skilled professional with hands-on knowledge on multiple tech stacks like Clouds (AWS, Azure, GCP), 
    Machine Learning Development and with a proven track record of successfully implementing end-to-end ML 
    solutions & AI automated solutions. Proficient in Python & R programming and AWS services. Strong 
    analytical and problem-solving abilities, coupled with excellent communication skills.
    """
    # st.write(content)
    st.info(content)