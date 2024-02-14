import streamlit as st
from PIL import Image


st.title("Artificial Intelligence and Testing")
#st.set_page_config(page_title="My Profile", page_icon=":tada", layout='wide')
image_kmeans_form = Image.open("images/kmeans1.jpg")
image_silhoutte_form = Image.open("images/Silhouette plot.png")
# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

option = st.selectbox('Unsupervised',('KMeans'))
with st.container():
        st.write("---")
        st.header("Validating KMeans clustering")
        #st.write('##')
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(image_kmeans_form)
        with text_column:
            #st.subheader("KMeans Clustering")
            st.write("""K-means clustering is one of the simplest and popular unsupervised machine learning algorithms. You’ll define a target number k, which refers to the number of centroids you need in the dataset. A centroid is the imaginary or real location representing the center of the cluster. Every data point is allocated to each of the clusters through reducing the in-cluster sum of squares. In other words, the K-means algorithm identifies k number of centroids, and then allocates every data point to the nearest cluster, while keeping the centroids as small as possible. 
                     The ‘means’ in the K-means refers to averaging of the data; that is, finding the centroid.""")
with st.container():
            st.write("Now the question is, how do we actually determine the number of clusters we have choosen is correct or not?")

with st.container():
     st.header("Silhouette coefficient")
     st.write("""Silhouette refers to a method of interpretation and validation of consistency within clusters of data.
              The silhouette value is a measure of how similar an object is to its own cluster (cohesion) compared to other clusters (separation). The silhouette ranges from −1 to +1, where a high value indicates that the object is well matched to its own cluster and poorly matched to neighboring clusters. 
              If most objects have a high value, then the clustering configuration is appropriate.""")
     st.write("How it works?")
     st.write(
            """
            - For each data point, the silhouette coefficient is calculated. This coefficient ranges from -1 to 1, where
            - 1: The point is well-clustered, meaning it is far away from points in other clusters and close to points in its own cluster
            - 0: The point is on the border of two clusters, and it's unclear which cluster it belongs to.
            - -1: The point is poorly clustered, meaning it is closer to points in other clusters than to points in its own cluster
            - The average silhouette coefficient across all data points is then calculated. This score provides an overall 
              measure of the quality of the clustering. Higher scores indicate better clustering. """)
     st.write("""Visualization:

Silhouette analysis can also be visualized using a silhouette plot. This plot shows the silhouette coefficient for each data point, along with its cluster assignment. A good silhouette plot will have most points with silhouette coefficients close to 1, indicating that they are well-clustered.
Image of Silhouette plot in clusteringOpens in a new window""")
 
     st.image(image_silhoutte_form)

     st.write("""Interpretation:

A silhouette score of more than 0.7 is considered to be strong, indicating that the clusters are well-separated.
A score between 0.5 and 0.7 is considered to be reasonable.
A score below 0.5 indicates that the clusters may not be well-separated, and you may want to try a different clustering algorithm or number of clusters.
              
Limitations:

1. Silhouette analysis is sensitive to the distance metric used.
              
2. It may not be suitable for data with highly irregular-shaped clusters.
              """)
             
     
     
            



        
