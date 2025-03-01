import streamlit as st

def app():
    st.title('Sustainability Donation and Distribution System for People with Disabilities')
    
    # Introduction section
    st.write('This application has been made by Sharon, Mitchell and Loice, a GZU students dedicated to creating impactful solutions.')
    
    # App functionality section
    st.header('App Functionality')
    st.write('''
    - **Disability Classification**: Utilizes image processing to classify the type of disability.
    - **Needs Recommendation**: Recommends necessary aids based on the classification results.
    - **Exploratory Data Analysis (EDA)**: Performs EDA to understand data trends and patterns.
    - **Donor Outreach**: Connects with potential donors to support the cause.
    - **Automated Donation**: Features an automated donation page where parameters can be set to determine specific needs.
    ''')
    
    # Footer section
    st.write('---')
    st.write('Thank you for visiting our app. Your support helps us make a difference in the lives of many.')
