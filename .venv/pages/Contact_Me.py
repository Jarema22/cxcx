import streamlit as st
import smtplib, ssl
import os




def Send_Email(massage):
    host = 'smtp.gmail.com'
    port = 465
    username = "python.test.app228@gmail.com"

    password = "yfbk qqnf zwsn yznq"

    receiver = "python.test.app228@gmail.com"
    context = ssl.create_default_context()
    print(massage)
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        print(massage)
        server.login(username, password)
        server.sendmail(username, receiver, massage)
        print("dan")

st.header("Contact Me")

with st.form(key ="my_form"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your Message")
    message = f"""\
Subject: New email from:{user_email}

From {user_email}
{raw_message}
"""
    submit_button = st.form_submit_button("Submit")
    print(submit_button)
    if submit_button:
        Send_Email(message)
        st.info("Your emile was sent successfully ")

        