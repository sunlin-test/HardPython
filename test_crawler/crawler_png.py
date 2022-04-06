import pytesseract
from PIL import Image

img = Image.open('./test.png')
img = img.convert('L')
code = pytesseract.image_to_string(img)
print(code)