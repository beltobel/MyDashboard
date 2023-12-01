import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# local_css("style/style.css")

st.set_page_config(
    page_title="10Academy",
    page_icon="👋",
)

st.title("Main Page")

st.sidebar.success("Select a page above.")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----

#animation
lottie_coding = load_lottieurl("https://lottie.host/7d1337be-f11c-41bc-a85e-3ab13e2230b2/E15cEsqRLc.json")


# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Slack Message Analysis")
        st.write("")
        st.write(
            """
            10 Academy provides comprehensive training programs, mentoring, and community support for young
            Africans to excel in their careers. 
            
            """
        )
       
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding") #animation landed here
        st.write("---")

