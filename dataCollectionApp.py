import streamlit as st
import csv

# Define the data structure
class DisabledIndividual:
    def __init__(self, name, age, gender,
                 marital_status, has_children, 
                 work, talent, school, disability_type, 
                 specific_needs, other_info):
        self.name = name
        self.age = age
        self.gender = gender
        self.marital_status = marital_status
        self.has_children = has_children
        self.work = work
        self.talent = talent
        self.school = school
        self.disability_type = disability_type
        self.specific_needs = specific_needs
        self.other_info = other_info

# Create a data collection function
def collect_data():
    st.header("Personal Information")
    name = st.text_input("Name:")
    age = st.number_input("Age:")
    gender = st.selectbox("Gender:", ["Male", "Female", "Other"])
    
    st.header("Family and Marital Status")
    has_children = st.checkbox("Has Children?")
    marital_status = st.selectbox("Marital Status:", ["Single", "Married", "Divorced", "Widowed"])
    
    st.header("Education and Work")
    school = st.text_input("School/Educational Institution:")
    work = st.text_input("Current Work/Occupation:")
    
    talent = st.text_input("Special Talents/Skills:")

    st.header("Disability Information")
    disability_type_options = ["Physical Disability", "Visual Impairment", "Hearing Impairment", "Intellectual Disability", "Neurodevelopmental Disorder", "Other"]
    disability_type = st.multiselect("Disability Type:", disability_type_options, default="Physical Disability")

    other_disability_type = ""
    if "Other" in disability_type:
        other_disability_type = st.text_input("Other Disability Type:")

    st.header("Specific Needs")
    specific_needs = []
    num_needs = st.number_input("Number of Specific Needs:", min_value=1, value=1, step=1)
    for i in range(num_needs):
        need = st.text_input(f"Specific Need {i+1}:")
        specific_needs.append(need)
   
    st.header("Additional Information")
    other_info = st.text_area("Other Relevant Information:")

    return DisabledIndividual(name, age, gender,
                 marital_status, has_children, 
                 work, talent, school, disability_type, 
                 specific_needs, other_info)

# Store the collected data
def store_data(record):
    with open('data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            record.name, record.age, record.gender, '|'.join(record.disability_type),
            '|'.join(record.specific_needs), record.school, record.work,
            record.talent, record.has_children, record.marital_status,
            record.other_info
        ])

# Streamlit app
def main():
    st.title("Data Collection for Disabled Individuals")
    
    with st.form("data_form"):
        individual = collect_data()
        submit_button = st.form_submit_button(label="Submit")
    
    if submit_button:
        store_data(individual)
        st.success("Data submitted successfully!")
        st.form_submit_button("Reset Form")
        st.experimental_rerun()

if __name__ == '__main__':
    main()