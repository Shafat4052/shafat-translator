from flask import Flask, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/')
def home():
    return app.send_static_file('indexx.html')

@app.route('/translate', methods=['POST'])
def translate_my_text():
    data = request.json
    text_to_translate = data['text']
    source_lang = data['source'] 
    target_lang = data['target'] 
    
    try:

        translator = GoogleTranslator(source=source_lang, target=target_lang)
        result = translator.translate(text_to_translate)
        
        if result:
            return jsonify({'translated_text': result})
        else:
            return jsonify({'translated_text': "Sorry, could not translate this specific text."})
            
    except Exception as e:
        print(f"Error: {e}") # Yeh terminal mein error dikhayega
        return jsonify({'translated_text': "Kashmiri translation is currently loading, try again!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)