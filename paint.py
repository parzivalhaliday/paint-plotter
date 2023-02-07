# Code to color a image in the Paint application using PyAutoGUI

import pyautogui as pag
from PIL import Image
import time
import requests
import io
import pandas

# Fetch the image from the URL
response = requests.get('image link')
image_byte = io.BytesIO(response.content)
foto = Image.open(image_byte)

# Convert the image to grayscale
foto = foto.convert('L')

# Resize the image to reduce the processing time
oran = 0.5
foto = foto.resize((int(foto.size[0]*oran),int(foto.size[1]*oran)))
x,y = foto.size

# Get the data from the image
fotodata = foto.getdata()

# Store the coordinate and color data in two separate lists
xsayac = 0
ysayac = 0
koordinat = []
renk = []
for data in fotodata:
    renk.append(data)
    koordinat.append((xsayac, ysayac))
        
    xsayac = xsayac + 1
    if xsayac == x:
        xsayac = 0
        ysayac += 1

# Store the coordinate and color data in a dataframe
bilgiler = {'koordinat':koordinat, 'renk':renk}
dataframe = pandas.DataFrame(bilgiler).sort_values('renk')

# Set the initial color value to 0
renkkodu = 0

# Loop through the sorted dataframe and color each pixel
sayac = 0
for i in zip(dataframe['koordinat'], dataframe['renk']):
    sayac += 1
    start = time.time()
    
    # Check if the color value has changed
    if renkkodu != i[1]:
        renkkodu = i[1]
        # Click the color select button
        pag.click(1060, 75)

        # Wait for the color select dialog to appear
        time.sleep(0.05)
        
        # Enter the color values in the dialog
        pag.click(1165, 595)
        for _ in range(3):
            pag.press('backspace')
            time.sleep(0.05)
        pag.typewrite(str(i[1]))

        pag.click(1165, 620)
        for _ in range(3):
            pag.press('backspace')
            time.sleep(0.05)
        pag.typewrite(str(i[1]))

        pag.click(1165,640)
        for _ in range(3):
            pag.press('backspace')
            time.sleep(0.05)
        pag.typewrite(str(i[1]))

        # Click the 'OK' button
        pag.click(777, 665)
        time.sleep(0.05)
    
    # Click the current pixel
    pag.click(8 + i[0][0], 147 + i[0][1])
