from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from googletrans import Translator

app = Flask(__name__)
CORS(app)

languages = [
    ("Arabic", "ar", "عربي"),
    ("French", "fr", "فرنسي"),
    ("Chinese", "zh-CN", "الصينية"),
    ("Persian", "fa", "الفارسية"),
    ("Turkish", "tr", "التركية"),
    ("Bangla", "bn", "البنغالية"),
    ("German", "de", "المانية"),
    ("Hindi", "hi", "الهندية"),
    ("Italian", "it", "ايطالي"),
    ("Japanese", "ja", "اليابان"),
    ("Portuguese", "pt", "البرتغالية"),
    ("Russian", "ru", "الروسية"),
    ("Spanish", "es", "الأسبانية"),
    ("Urdu", "ur", "الأردية")
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_translator', methods=['GET'])
def get_translator():
    text = request.args.get('text')
    try:
        translated = translate(text)
        return jsonify({"is_finished": True, "data": translated})
    except:
        return jsonify({"is_finished": False, "utext": ""})

def translate(text):
    translator = Translator()
    translations = []
    for language, code, name_ar in languages:
        translated_text = translator.translate(text, src='en', dest=code).text
        translations.append((language, translated_text, code, name_ar))
    return translations

if __name__ == '__main__':
    app.run(debug=True)
