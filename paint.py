import pyautogui as pag
from PIL import Image
import time
import requests
import io
import pandas

response = requests.get('https://cdn.discordapp.com/attachments/775687593030713364/814488487348797461/ask.jpg')
image_byte = io.BytesIO(response.content)
foto = Image.open(image_byte)

foto = foto.convert('L')

oran = 0.5
foto = foto.resize((int(foto.size[0]*oran),int(foto.size[1]*oran)))
x,y = foto.size

print(x,y)
input('hazır olunca entere bas\n')

xsayac = 0
ysayac = 0

pag.PAUSE = 0.0005

koordinat = []
renk = []

fotodata = foto.getdata()

for data in fotodata:
    renk.append(data)
    koordinat.append((xsayac, ysayac))
        
    xsayac = xsayac + 1
    if xsayac == x:
        xsayac = 0
        ysayac += 1

bilgiler = {'koordinat':koordinat, 'renk':renk}
dataframe = pandas.DataFrame(bilgiler).sort_values('renk')

renkkodu = 0
sayac = 0
for i in zip(dataframe['koordinat'], dataframe['renk']):
    sayac += 1
    start = time.time()
    print(i[0], i[1])
    print(sayac / (x*y) )
    print('-'*35)
    
    if renkkodu != i[1]:
        renkkodu = i[1]
        # Renk Seçimine tıkla
        pag.click(1060, 75)

        time.sleep(0.05)
        # Renk ayarlarını gir
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

        # Tamam'a Tıkla
        pag.click(777, 665)
        time.sleep(0.05)
    
    pag.click(8 + i[0][0], 147 + i[0][1])