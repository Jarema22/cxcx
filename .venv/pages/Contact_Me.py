import streamlit as st
import Contact_ME  as c


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
        c.Send_Email(message)
        st.info("Your emile was sent successfully ")

        