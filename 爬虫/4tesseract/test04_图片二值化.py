import pytesseract
from PIL import Image


# 二值化
def convert_img(img, threshold):
    img = img.convert("L")  # 处理灰度
    pixels = img.load()
    for x in range(img.width):
        for y in range(img.height):
            if pixels[x, y] > threshold:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0
    img.show()
    return img


# 打开图片
captcha = Image.open("3.png")
convert_img(captcha, 150)
# 识别
result = pytesseract.image_to_string(captcha)
print(result)
