import pytesseract
from PIL import Image
import os
import sys


img = Image.open(sys.argv[1])
w, h = img.size
img.crop((50, 50, 700, 150)).save("cp.jpg")
img.crop((200, 600, 500, 650)).save("hp.jpg")
img.crop((300, 850, 450, 950)).save("sd.jpg")

print(pytesseract.image_to_string(Image.open("hp.jpg")))
print(pytesseract.image_to_string(Image.open("cp.jpg")))
print(pytesseract.image_to_string(Image.open("sd.jpg")))

os.remove("cp.jpg")
os.remove("hp.jpg")
os.remove("sd.jpg")
