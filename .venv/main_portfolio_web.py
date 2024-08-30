import streamlit as st
from pygments.styles.dracula import yellow
st.set_page_config(layout="wide")
col1 ,col2 =st.columns(2)

with col1:
    st.image("/home/stranger/Documents/python/app1/pythonProject1/images/among-us-5825180_1280.jpg", width=600)
with col2:
    st.title("Panio Jarema")
    content = """
    I am Just NOOB
    """
    st.info(content)