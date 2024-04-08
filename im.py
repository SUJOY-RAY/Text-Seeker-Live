from PIL import Image
import pytesseract

image = Image.open('/home/arclight/Coding/Machine Learning in python/Text-Seeker-Live/images.png')

# Perform OCR using PyTesseract
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)