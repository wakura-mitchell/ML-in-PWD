import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    # Code for data analysis
    st.title("Data Analysis")

    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    if uploaded_file is not None:
        # Read the uploaded file into a DataFrame
        data = pd.read_csv(uploaded_file)
        # Display a preview of the data
        st.write("Preview of the data:")
        st.write(data.head())

        # Data Visualization section
        st.write("Data Visualization:")
        # Let the user select columns to plot
        columns_for_visualization = st.multiselect("Select column/s for data visualization", data.columns)

        # Plotting each selected column
        for col in columns_for_visualization:
            # Data visualization
            plt.figure(figsize=(6,6))
            sns.countplot(x=col, data=data)
            plt.xlabel(f"Distribution of {col}")
            st.pyplot(plt.gcf())
            plt.close()

        # Pie chart analysis section
        st.write("Pie chart analysis:")
        # Let the user select columns for the pie chart
        column_name1 = st.multiselect("Select column/s for Pie chart", data.columns)

        if column_name1:
            # Calculate the count of each unique value in the specified column
            value_counts1 = data[column_name1[0]].value_counts()

            # Plot the pie chart
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.pie(value_counts1, labels=value_counts1.index, autopct='%1.1f%%')
            ax.set_title(f'Pie Chart of {column_name1[0]}')
            ax.axis('equal')

            st.pyplot(fig)
    else:
        # Prompt the user to upload a file if none has been uploaded
        st.info("Please upload a CSV file to proceed with data analysis.")
