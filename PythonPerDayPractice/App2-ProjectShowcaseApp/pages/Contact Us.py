import sys
sys.path.append('E:\Job & Interview Kit\Revision Material\DS & Algos - Python & JavaScript\PythonPractise2024\PythonPerDayPractice')
import utilities
import streamlit as st

st.title("Contact Me")

with st.form(key="contact_form"):
    input_txt = st.text_input("Email Id")
    message = st.text_area("Enter Your Message....")
    button = st.form_submit_button("Send")
    if button:
        print("Button Clicked:")
        message = f"Subject: REVERT BACK - Email Recieved From an App !!\n"\
                  f"Hi,\n\nA user of your apps has tried to reach you. \n"\
                  f"Kindly go through the message & revert back accordingly. \n"\
                  f"\nMessage:\n{message}\n\nFrom: {input_txt}"
        utilities.send_email(message=message)
        st.info("Message is sent successfully !")
        
