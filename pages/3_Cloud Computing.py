import streamlit as st
from PIL import Image


st.title("Cloud Computing (will be updating shortly)")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


with st.container():
        st.write("---")