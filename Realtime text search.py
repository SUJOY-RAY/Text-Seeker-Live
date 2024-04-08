import cv2
import pytesseract
import numpy as np
import webbrowser
import re
from PIL import Image




# font_scale=1.5
# font=cv2.FONT_HERSHEY_SIMPLEX
# cap=cv2.VideoCapture(1)


# # # If the default camera is not available
# # if not cap.isOpened():
# #     cap=cv2.VideoCapture(0)   
# # else:
# #     raise IOError("Camera in-accessible")


# # counter=0
# # imageCharacter=""
# # while True:
# #     ret,frame=cap.read()
# #     counter+=1
# #     if (counter%20)==0:
# #         imgH,imgW,_ =frame.shape
        
# #         x1,y1,w1,h1=0,0,imgH,imgW
        
        
# #         rawText=pytesseract.image_to_string(frame)
# #         imageCharacter=re.sub(r'[^a-zA-Z0-9\s]', '', rawText)
# #         imageCharacter=imageCharacter.replace('?','')
# #         imageCharacter=imageCharacter.replace('/','')
        
        
# #         imageBoxes=pytesseract.image_to_boxes(frame)
        
        
# #         for boxes in imageBoxes.splitlines():
# #             boxes = boxes.split(' ')
# #             x,y,w,h = int(boxes[1]), int(boxes[2]), int(boxes[3]), int(boxes[4])
# #             cv2.rectangle(frame, (x, imgH-y), (w,imgH-h), (0,0,255),1)
        
        
# #         cv2.putText(frame, imageCharacter, (x1 + int(w1/2), imgH-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)
        
# #         font=cv2.FONT_HERSHEY_SIMPLEX
        
# #         cv2.imshow('Text Detection Tutorial',frame)

# #         if cv2.waitKey(2) & 0xFF == ord('q'):
# #             break



# # cap.release()
# # cv2.destroyAllWindows()

from tkinter import filedialog
import tkinter as tk


def select_file():
    global fil
    global myText
    file_path = filedialog.askopenfilename()
    if file_path:
        label.config(text="Selected file: " + file_path)
        fil=file_path
        myText=pytesseract.image_to_string(fil)
        label.config(text="Extracted Text: "+myText)
        

def searcher(myText):
        search_url=f"https://www.google.com/search?q={myText}"
        webbrowser.open(search_url)

    

root = tk.Tk()
root.title("File Selector")

label = tk.Label(root, text="No file selected")
label.pack(pady=20)

button = tk.Button(root, text="Select File", command=select_file)
button.pack(pady=10)

def perform_search():
    if myText:
        searcher(myText)
    else:
        label.config(text="No text extracted from file!")

button=tk.Button(root, text="Web Search", command=perform_search)
button.pack(pady=10)

root.mainloop()







