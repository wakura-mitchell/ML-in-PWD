import streamlit as st
import tensorflow as tf
from PIL import Image
import cv2
import numpy as np

def app():
    # Load your model
    modelPath = './models/'
    @st.cache_data #(allow_output_mutation=True)
    def load_model():
        model = tf.keras.models.load_model(modelPath + 'disabilityModel.keras')
        return model

    with st.spinner('Model is being loaded..'):
        model = load_model()

    # Define class names
    class_names = ['blind', 'crippled', 'deformed']

    # Main Streamlit app
    st.write("""
    # Sustainability Donation and Distribution System for People with Disabilities
    """)

    file = st.file_uploader("Please upload a picture", type=["jpg", "png"])

    def import_and_predict(image_data, model):
        size = (244, 244)  # model input size 
        image = image_data.resize(size, resample=Image.BILINEAR) 
        img = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
        img_reshape = img[np.newaxis, ...]
        prediction = model.predict(img_reshape)
        return prediction

    if file is None:
        st.text("Please upload an image file")
    else:
        image = Image.open(file)
        st.image(image, use_column_width=True)
        predictions = import_and_predict(image, model)
        score = tf.nn.softmax(predictions[0])
        class_name = class_names[np.argmax(score)]
        confidence = 100 * np.max(score)
        #st.write(f"This person is a {class_name} person with a {confidence:.2f}% confidence.")
        
        if class_name == 'crippled':
            st.write(f"This person is {class_name} and needs: wheel chair, straps, TEO")
            
        if class_name == 'blind':
            st.write(f'This person is {class_name} and needs: walking crane, shades, TEO')
            
        if class_name == 'deformed':
            st.write(f'This person is {class_name} and needs: wheel chair, straps, IC')
