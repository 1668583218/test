import pytesseract
from PIL import Image

img = Image.open("test01.png")
print(pytesseract.image_to_string(img, lang='chi_sim'))
