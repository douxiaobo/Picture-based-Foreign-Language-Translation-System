from flask import Flask, jsonify, render_template, request
import pytesseract
from PIL import Image
import pytesseract
from googletrans import Translator
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
PORT = 8010

@app.route('/api/translateimagetext', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        # return render_template('translateimagetext.html')
        return jsonify({'text':0, 'result':0})  
    
    image = request.files.get('image')
    image.save('image.png')

    origin_language = request.form.get('origin_language')
    target_language = request.form.get('target_language')
    # data = request.form
    # origin_language = data['origin_language']
    # target_language = data['target_language']

    
    # origin_text = pytesseract.image_to_string(Image.open('image.png'),lang='chi_sim') 
    if origin_language is None or origin_language == '':
        origin_text = pytesseract.image_to_string(Image.open('image.png'))
    else: 
        origin_text = pytesseract.image_to_string(Image.open('image.png'),lang=origin_language)


    translator = Translator()

    # origin_language = translator.detect(origin_text)
    # origin_language = origin_language.lang

    # target_text = translator.translate(origin_text,dest='en')
    target_text = translator.translate(origin_text,dest=target_language)
    # print(result.text)

    # return render_template('translateimagetext.html', text = origin_text, result=target_text.text)
    return jsonify({'origin_language':origin_language, 'origin_text':origin_text, 'target_language':target_language, 'target_text':target_text.text})


if __name__ == '__main__':
    app.run(port=int(PORT), debug=True)

