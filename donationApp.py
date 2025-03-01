import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import pickle
from sklearn.preprocessing import LabelEncoder

def main():
    
    le = LabelEncoder()
    
    st.title("Donation and Distribution App for the disabled")
    
    model = pickle.load(open('./Random forest Model.pkl', 'rb'))

    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)


    st.title('Automatic Distribution')

    # Define your columns
    col1, col2, col3 = st.columns(3)

    le = LabelEncoder()

    with col1:
        age = st.text_input('Age')
            
    with col1:
        has_children = st.checkbox("Has Children?")
        # Convert boolean checkbox to int
        has_children_encoded = int(has_children)
        
    with col1:
        FamilySize = st.text_input('Family Size')
            
    with col1:
        school = st.selectbox('Issues regarding school:', ["financial barriers", "learning disabilities", "lack of access to proper education"])
        # Fit label encoder and return encoded labels
        school_encoded = le.fit_transform([school])
            
    with col1:
        FoodIssues = st.selectbox('Issues regarding food:', ["nutritional deficiencies", "limited access to healthy food", "food insecurity "])
        # Fit label encoder and return encoded labels
        FoodIssues_encoded = le.fit_transform([FoodIssues])

    with col2:
        finsitu = st.selectbox("Financial Situation:", ["unemployed", "below poverty line", "low-income"])
        # Fit label encoder and return encoded labels
        finsitu_encoded = le.fit_transform([finsitu])

    with col2:
        work = st.selectbox('Work Status:', ['Employed', 'Unemployed'])
        # Fit label encoder and return encoded labels
        work_encoded = le.fit_transform([work])
            
    with col2:
        Disability = st.selectbox('Disability type:', ["Mental health condition", "physical disability", "visual impairment "])
        # Fit label encoder and return encoded labels
        disability_type_encoded = le.fit_transform([Disability])
            
    with col2:
        Dependents = st.text_input('Dependents: ')
        
    with col2:
        MonthlyIncome = st.text_input('Monthly Income: ')

    with col3:
        HighestLevelofSchoolAttained = st.selectbox('Highest Level of School Attained: ', ['secondary school', 'high school', 'university', 'primary school '])
        # Fit label encoder and return encoded labels
        HighestLevelofSchoolAttained_encoded = le.fit_transform([HighestLevelofSchoolAttained])
        
    with col3:
        Talent = st.selectbox('Talent type:', ["musical talent", "technical skills", "artistic abilities"])
        # Fit label encoder and return encoded labels
        talent_encoded = le.fit_transform([Talent])
        
    with col3:
        living_status = st.selectbox("Living Status:", ["homeless", "temporary housing", "shelter"])
        # Fit label encoder and return encoded labels
        living_status_encoded = le.fit_transform([living_status])
        
    with col3:
        MedicalCondition = st.text_input('Number of Medical Condition')
        
    with col3:
        LanguageProficiency = st.selectbox("Language Proficiency:", ["bilingual", "local language", "English"])
        # Fit label encoder and return encoded labels
        LanguageProficiency_encoded = le.fit_transform([LanguageProficiency])
        

    # code for Prediction
    special_need = ''

    # creating a button for Prediction

    if st.button('Check donation eligibility'):

        user_input = [age, MedicalCondition, FamilySize, school_encoded, talent_encoded, work_encoded, has_children_encoded, MonthlyIncome,
                    FoodIssues_encoded, HighestLevelofSchoolAttained_encoded, LanguageProficiency_encoded,
                    Dependents, living_status_encoded, disability_type_encoded, finsitu_encoded]

        user_input = [float(x) if x else 0 for x in user_input]

        special_need = model.predict([user_input])

        st.write('Predicted need:', special_need)


if __name__ == "__main__":
    main()