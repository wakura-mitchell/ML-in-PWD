import pandas as pd
import random

# Define the number of records in the dataset
num_records = 10000

# Define the list of attributes
attributes = ['Name', 'Age', 'Location', 'Latitude', 'Longitude', 'Financial Situation', 'Living Status', 'Occupation Status',
              'Disability', 'School Issues', 'Family Size', 'Dependents', 'Medical Conditions',
              'Monthly Income', 'Education Level', 'Language Proficiency', 'Talent',
              'Highest Level of School Attained', 'Food Issues', 'Assistance Package']

# Define the list of possible values for each attribute
financial_situation_options = ['low-income', 'unemployed', 'below poverty line']
living_status_options = ['homeless', 'shelter', 'temporary housing']
occupation_status_options = ['employed', 'unemployed', 'seeking employment']
disability_options = ['physical disability', 'visual impairment', 'mental health condition']
school_issues_options = ['lack of access to proper education', 'financial barriers', 'learning disabilities']
education_level_options = ['no formal education', 'primary school', 'secondary school', 'university']
language_proficiency_options = ['English', 'local language', 'bilingual']
talent_options = ['artistic abilities', 'musical talent', 'technical skills']
highest_school_attained_options = ['primary school', 'secondary school', 'high school', 'university']
food_issues_options = ['food insecurity', 'limited access to healthy food', 'nutritional deficiencies']
assistance_package_options = ['Monetary Aid', 'Basic Necessities', 'Education and Skill Development',
                              'Healthcare Support', 'Job Placement and Career Support',
                              'Mental Health and Counseling Services']

# Define the latitude and longitude ranges for Zimbabwe rural areas
latitude_range = (-22.0, -15.5)
longitude_range = (25.0, 34.0)

# Initialize an empty list to hold the data records
data = []

# Generate synthetic data for each record
for _ in range(num_records):
    name = f'Person {_ + 1}'
    age = random.randint(18, 65)
    location = 'Zimbabwe Rural Area'
    latitude = round(random.uniform(latitude_range[0], latitude_range[1]), 4)
    longitude = round(random.uniform(longitude_range[0], longitude_range[1]), 4)
    financial_situation = random.choice(financial_situation_options)
    living_status = random.choice(living_status_options)
    occupation_status = random.choice(occupation_status_options)
    disability = random.choice(disability_options)
    school_issues = random.choice(school_issues_options)
    family_size = random.randint(1, 6)
    dependents = random.randint(0, family_size)
    medical_conditions = random.randint(0, 3)
    monthly_income = random.randint(0, 500)
    education_level = random.choice(education_level_options)
    language_proficiency = random.choice(language_proficiency_options)
    talent = random.choice(talent_options)
    highest_school_attained = random.choice(highest_school_attained_options)
    food_issues = random.choice(food_issues_options)
    assistance_package = random.choice(assistance_package_options)
    
    record = [name, age, location, latitude, longitude, financial_situation, living_status, occupation_status, disability, school_issues,
              family_size, dependents, medical_conditions, monthly_income, education_level, language_proficiency,
              talent, highest_school_attained, food_issues, assistance_package]
    data.append(record)

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=attributes)

# Export the DataFrame to a CSV file
df.to_csv('synthetic_dataset.csv', index=False)
