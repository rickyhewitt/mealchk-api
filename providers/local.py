# mealchk-cli
# providers/local.py
# ricky@rickyhewitt.dev

import pytesseract
from PIL import Image
import numpy as np

# Provider must feature an image_to_string function
def image_to_string(file_i):
    print("Provider: local (pytesseract)")

    img = np.array(Image.open(file_i))
    return pytesseract.image_to_string(img)