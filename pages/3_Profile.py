import streamlit as st
from PIL import Image

st.title("My Profile")
#st.set_page_config(page_title="My Profile", page_icon=":tada", layout='wide')
image_patent_form = Image.open("images/patent.jpg")
image_aicert_form = Image.open("images/aicert.png")
image_redhat_form = Image.open("images/redhat.png")


url="https://www.credly.com/organizations/brightest/"
redhaturl="https://www.redhat.com/en"


with st.container():
        st.write("---")
        st.header("My Patent")
        st.write('##')
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(image_patent_form)

        with text_column:
            st.subheader("SECURITY ORCHESTRATION, AUTOMATION, AND RESPONSE (SOAR) PLAYBOOK GENERATION")
            st.write("""
                     Neural network based solution to generate SOAR playbooks as part of remediation actions for any new 
                     security alerts/incidents/cases created in SOC environment.
                     Filed on September 26/2023 (18/372775)
                """)
            
with st.container():
        st.write("---")
        st.header("AiU - Certified Tester in Artificial Intelligence (CTAI)")
        st.write('##')
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(image_aicert_form)

        with text_column:
            st.write("Issed by [Brightest](%s)" % url)
            st.write("""
                    Holders of this badge understand what Artificial Intelligence is and are able to comprehend and relate theoretical concepts and practical applications of Machine Learning (ML).
                     """)


with st.container():
        st.write("---")
        st.header("RHEL 6.1 Certified EngineerRHEL 6.1 Certified Engineer")
        st.write('##')
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(image_redhat_form)

        with text_column:
            st.write("Issed on Feb 2013 by Red Hat, certificate number:130-034-010")
            




