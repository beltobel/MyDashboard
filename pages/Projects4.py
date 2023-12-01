import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import requests
from streamlit_lottie import st_lottie
from PIL import Image

# local_css("style/style.css")

img_contact_form = Image.open("images/data_science.jpg")
img_lottie_animation = Image.open("images/eda.jpg")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")
   
        
with st.container():
    st.header("task-4")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Dashboards")
        st.write(
            """
           
            """
        )
#         st.markdown("[Details...]()")

        