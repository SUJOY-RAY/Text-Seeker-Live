# Text-Seeker-Live

This Python script captures video frames from a camera, performs Optical Character Recognition (OCR) using Tesseract, and displays the processed frames with bounding boxes around detected text. Additionally, it extracts the recognized text, cleans it, and performs a Google search using the cleaned text.

## Prerequisites

- Python 3.x
- OpenCV
- pytesseract
- Tesseract OCR
- Numpy
- Pillow (PIL)

## Installation

1. Install Python from [python.org](https://www.python.org/).
2. Install required Python packages using the following command:

   ```
   pip install opencv-python pytesseract numpy Pillow
   ```

3. Install Tesseract OCR by following the instructions at [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract).

## Usage

1. Set the path to the Tesseract executable in the code:

   ```python
   pytesseract.pytesseract.tesseract_cmd = 'path_to_tesseract_exe'
   ```

2. Run the script:

   ```
   python Text-Seeker-Live.py
   ```

3. The script will open a video capture window displaying processed frames with text and bounding boxes.
4. Press 'q' to exit the application and start the web search.

## Notes

- The script assumes the presence of a camera. It uses camera 1 by default and falls back to camera 0 if camera 1 is not available.
- The Google search is performed using the cleaned text extracted from the frames.
