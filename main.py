import os
from pdf2image import convert_from_path
import numpy as nm
import re
import pytesseract
import cv2
from PIL import ImageGrab, Image
import shutil

# For colored outputs
import colorama
from colorama import Fore, Back, Style
colorama.init()

def clear():
    os.system('cls')


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

my_list = os.listdir('Group A')
if not os.path.exists('Group A - conv'):
    os.mkdir('Group A - conv')
for file in my_list:

    images = convert_from_path('./Group A/'+file,
                               poppler_path=r"D:\Downloads\Release-21.03.0\poppler-21.03.0\Library\bin", grayscale=True, dpi=20)
    image = (images[0])
    image = image.crop((20, 120, 382, 155))
    tesstr = pytesseract.image_to_string(nm.array(image), lang='eng')
    tesstr = tesstr.strip()
    shutil.copy('./Group A/'+file, './Group A - conv/'+tesstr+'.pdf')
    print(Fore.BLUE+"\u2713 Copied "+tesstr+'.pdf')
print(Fore.GREEN+"\u2713\u2713 All files copied successfully!")
