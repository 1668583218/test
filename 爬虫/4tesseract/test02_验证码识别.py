import pytesseract
from PIL import Image

captcha = Image.open("1.png")
result = pytesseract.image_to_string(captcha)
print(result)
