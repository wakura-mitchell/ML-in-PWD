import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def app():
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
    # Code for ask for donations
            # Get user input
        recipient_email = st.text_input("Recipient Email")
        subject = st.text_input("Email Subject")
        message = st.text_area("Email Message")

        # Load and display dataset
        st.subheader("Upload a dataset to plot")
        st.write(data.head())

        # Allow user to select columns to plot
        st.subheader("Select columns to plot")
        columns = data.columns.tolist()
        selected_columns = st.multiselect("Select columns", columns, default=columns[:2])

            # Plot the selected columns as pie charts
        for column_name in selected_columns:
                value_counts = data[column_name].value_counts()
                fig, ax = plt.subplots(figsize=(12, 6))
                ax.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%')
                ax.set_title(f'Pie Chart of {column_name}')
                ax.axis('equal')
                st.pyplot(fig)

        if st.button("Send Email"):
            try:
                # Set up email details
                msg = MIMEMultipart()
                msg['Subject'] = subject
                msg['From'] = "wakuramitchell@gmail.com"
                msg['To'] = recipient_email
                msg.attach(MIMEText(message + "\n\nPlease see the attached graphs for analysis."))

                for column_name in selected_columns:
                    plt.figure(figsize=(12, 6))
                    value_counts = data[column_name].value_counts()
                    plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%')
                    plt.title(f'Pie Chart of {column_name}')
                    plt.axis('equal')
                    plt.savefig(f"{column_name}_graph.png", format='png')
                    with open(f"{column_name}_graph.png", 'rb') as f:
                        img = MIMEImage(f.read())
                        img.add_header('Content-Disposition', 'attachment', filename=f"{column_name}_graph.png")
                        msg.attach(img)

                # Send the email
                with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
                    smtp.starttls()
                    smtp.login("example@gmail.com", "your_password")
                    smtp.send_message(msg)
                    
                st.success("Email sent successfully!")
            except Exception as e:
                st.error(f"Failed to send email: {e}")