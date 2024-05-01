import streamlit as st
import pandas as pd

loc = "E:\Job & Interview Kit\Revision Material\DS & Algos - Python & JavaScript\PythonPractise2024\PythonPerDayPractice\App5-CompanyWebsite"

# reading data.csv:
data = pd.read_csv(f"{loc}\data.csv")

# setting up page layout width
st.set_page_config(layout="wide")

# adding title
st.title("Tech Mettle")

# adding info
introduction = """
We specialize in providing cutting-edge software
services to empower businesses in the digital age. With a team of skilled
professionals and a commitment to excellence, we offer a comprehensive 
suite of solutions tailored to meet the evolving needs of our clients.
"""
our_services = """
<h4>Data Science:</h4> Unlock the power of data with our advanced analytics and data science services. From data mining and predictive modeling to machine learning and AI-driven insights, we help businesses leverage their data assets to make informed decisions and drive growth.

<h4>Artificial Intelligence:</h4> Stay ahead of the curve with our AI solutions designed to enhance efficiency, productivity, and innovation. Whether it's natural language processing, computer vision, or deep learning, we deliver AI-powered solutions that transform businesses and drive competitive advantage.

<h4>UI/UX Design:</h4> Create immersive and engaging user experiences with our UI/UX design services. Our team of designers combines creativity with usability to craft intuitive interfaces and seamless interactions that delight users and elevate your brand.

<h4>Due Diligence:</h4> Mitigate risks and make informed business decisions with our due diligence services. From financial analysis and market research to regulatory compliance and legal reviews, we provide comprehensive due diligence solutions to support your strategic objectives.

<h4>Talent Acquisition:</h4> Build a high-performing team with our talent acquisition services. We specialize in recruiting top-tier talent across various domains, including technology, data science, design, and business operations, to help you assemble a team that drives success.

"""
why_choose_us = """
<h4>Expertise:</h4> Our team comprises seasoned professionals with extensive experience in their respective fields, ensuring the highest level of quality and expertise in every project.

<h4>Innovation:</h4> We stay at the forefront of technology and innovation, constantly exploring new tools, techniques, and methodologies to deliver best-in-class solutions that drive results.

<h4>Client-Centric Approach:</h4> We prioritize client satisfaction and collaborate closely with our clients to understand their unique challenges, goals, and objectives, tailoring our solutions to meet their specific needs.

<h4>Results-Driven:</h4> We are committed to delivering tangible results and measurable outcomes that add value to our clients' businesses, driving growth, efficiency, and success.

"""
st.info(introduction)
st.header("Our Services")
st.write(our_services, unsafe_allow_html=True)
st.header("Why Choose Us?")
st.write(why_choose_us, unsafe_allow_html=True)
st.header("Our Team")

# ".columns" method will return three column objects
col1, col2, col3 = st.columns(3)

indice_len = int(len(data)/3)

with col1:
    for index, value in data[:indice_len].iterrows():
        st.header(f"{value['first name']} {value['last name']}")
        st.write(value["role"])
        st.image(f"{loc}\images\{value['image']}")

with col2:
    for index, value in data[indice_len:2*indice_len].iterrows():
        st.header(f"{value['first name']} {value['last name']}")
        st.write(value["role"])
        st.image(f"{loc}\images\{value['image']}")

with col3:
    for index, value in data[2*indice_len:].iterrows():
        st.header(f"{value['first name']} {value['last name']}")
        st.write(value["role"])
        st.image(f"{loc}\images\{value['image']}")















