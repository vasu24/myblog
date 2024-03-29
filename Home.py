import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# Function to get response from llama2
# https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Vasudevan Blog", page_icon=":tada", layout='wide')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

linkedinurl="https://www.linkedin.com/in/vasudevan-gajjala-16546715/"

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
#img_contact_form = Image.open("images/yt_contact_form.png")
#img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

with st.container():
    st.subheader("Hi, I am Vasudevan Gajjala :wave:")
    st.title("A Quality Engineer from India")
    
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write(
            """
            - I work in an MNC as a Quality Engineer
            - My professional interests are in Cloud Computing, Artifical Intelligence, so i keep exploring them
            - Looking for a way to leverage the power of Cloud Computing, Artificial Intelligence.
            - Want to learn Data Science to perform meaningful and impactful analyses. """)
        st.header("What I would like to share")    
        st.write(" Testing an Artificial Intelligence is bit different from traditional software testing. I would like to share the information about how can we test such kind of systems.")
        st.write("If this sounds intresting to you,please follow my blog and consider joining me over [linkedin](%s)" % linkedinurl)
    
    with right_column:
        st_lottie(lottie_coding,height=300,key="coding")





    




