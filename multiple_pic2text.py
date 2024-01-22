from PIL import Image
from pytesseract import pytesseract
import os


#Define path to images folder
path_to_images = r'bilder/'

os.remove(path_to_images + ".DS_Store")

#Get the file names in the directory
for root, dirs, file_names in os.walk(path_to_images):
    #Iterate over each file name in the folder
    for file_name in file_names:
        #Open image with PIL
        img = Image.open(path_to_images + file_name)

        #Extract text from image
        text = pytesseract.image_to_string(img)

        print(text)