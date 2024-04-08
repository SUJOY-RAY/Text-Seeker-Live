from PIL import Image
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'D:\\Python Projects\\pytesseract\\tesseract.exe'

text=cv2.imread("sxpra.png")

myText=pytesseract.image_to_string(text)

print(myText)