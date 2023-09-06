import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from keras.models import load_model
import cv2
import io

model = load_model('model5.h5')
# title 
st.set_page_config(page_title="Hotdog Not Hotdog App", page_icon="🌭")

# Define function to classify hotdog or not hotdog
def classify_image(image, model):
    new_image = []
    img_bytes = image.read()  # Read the binary content of the uploaded file
    img = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), 1)  # Decode the image from bytes
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (128, 128))
    img_array = np.array(img)
    new_image.append(img)
    img_array_norm = np.array(new_image) / 255
    preds = model.predict(img_array_norm)
    y_score = preds.ravel()
    y_preds = np.where(y_score > 0.5, 1, 0)
    if y_preds == 0:
        return "Hotdog"
    else:
        return "Not Hotdog"

def main():
    st.title("Hotdog Not Hotdog Classifier")
    st.write("Upload an image and let's find out if it's a hotdog or not!")

    background_image = Image.open("assets/background.jpg")
    st.image(background_image, use_column_width=True)

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        result = classify_image(uploaded_file, model)
        st.write(f"Prediction: This is {result}!")

if __name__ == "__main__":
    main()
