import pytesseract

from PIL import Image
from PIL import ImageFilter

image=Image.open('Github.png')

image =image.convert('L')

image=image.point(lambda x: 0 if x<128 else 255)

image=image.filter(ImageFilter.MedianFilter())

text=pytesseract.image_to_string(image);

print(text);