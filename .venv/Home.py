import streamlit as st
import pandas

from pygments.styles.dracula import yellow
from streamlit import image, empty

st.set_page_config(layout="wide")
col1 ,col2 =st.columns(2)

with col1:
    st.image("images/among-us-5825180_1280.jpg", width=600)
with col2:
    st.title("Panio Jarema")
    content = """
    I am Just NOOB
    """

    st.info(content)

content1 = """Below you can finde some of the apps I have built in Python. Feel free to contact me!"""
st.write(content1)

col3, empty_col, col4 = st.columns([1.5, 1.0, 1.5])

df = pandas.read_csv(".venv/data (2).csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")