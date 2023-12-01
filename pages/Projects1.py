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

# ---- PROJECTS ----
with st.container():
    st.write("")
    st.header("My Projects")
    st.header("task-1")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("EDA analysis ")
        st.write(
            """
            Anonymized Slack messages of Batch 6 from the 10 Academy training program. 
            The dataset is organised into folders, each representing a Slack channel, and
           contains JSON files for individual days.
           
           
           """
            
        )
        
        
#         st.markdown("[Details...]()")
        


              
        

