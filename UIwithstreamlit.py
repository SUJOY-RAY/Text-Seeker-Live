import streamlit as st
import pytesseract
import numpy as np
import webbrowser
from PIL import Image

def extract_Text(image):
    myText = pytesseract.image_to_string(image)
    st.write("Extracted Text:", myText)

def perform_search(myText):
    if myText:
        search_url = f"https://www.google.com/search?q={myText}"
        webbrowser.open(search_url)

st.title("Text Extraction and Search")


# select image from file explorer
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    button_clicked1 = st.button("Extract Text ")
    button_clicked2 = st.button("Search")
    if button_clicked1:
        perform_search(image)