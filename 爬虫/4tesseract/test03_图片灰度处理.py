import pytesseract
from PIL import Image

# 灰度处理
captcha = Image.open("3.png")
result = captcha.convert('L')
result.show()

# 识别
result = pytesseract.image_to_string(captcha)
print(result)
