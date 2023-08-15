from PIL import Image
import pytesseract
from googletrans import Translator
import re
import json


# 中转英
print("中文->英文————————————————————————————————————————")
img = Image.open('image_chi.jpg')
text = pytesseract.image_to_string(img,lang='chi_sim') 
# 默认是支持英文的，所以我们可以直接识别,要识别中文或其它语言时就需要指定
print(text)

# text = '你好，我喜欢吃饭和睡觉'

translator = Translator()
result = translator.translate(text,dest='en')
print(result.text)


# 试试英转中
print("英文->中文————————————————————————————————————————")
img = Image.open('image_en.png')
text2 = pytesseract.image_to_string(img) 
print(text2)

translator = Translator()
result2 = translator.translate(text2,dest='zh-CN')
print(result2.text)




# from googletrans import Translator
# # translator = Translator(service_urls=['translate.google.cn'])
# translator = Translator()
# source = '这是我写的简易翻译功能。'
# # text = translator.translate(source,src='zh-cn',dest='en').text
# text = translator.translate(source, dest='en')
# print(text)

