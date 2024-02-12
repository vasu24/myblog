import streamlit as st
from PIL import Image


st.title("AI - Testing space")
#st.set_page_config(page_title="My Profile", page_icon=":tada", layout='wide')
image_kmeans_form = Image.open("images/kmeans.png")


with st.container():
        st.write("---")
        st.header("Testing K-means clustering")
        st.write('##')
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(image_kmeans_form)
        with text_column:
            st.subheader("K-means clustering")
            st.write("""
                    k-means clustering is a method of vector quantization, originally from signal processing, 
                    that aims to partition n observations into k clusters in which each observation belongs to the 
                    cluster with the nearest mean (cluster centers or cluster centroid), serving as a prototype of the cluster.""")