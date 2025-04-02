from flask import Flask, request, jsonify
from translate import translate_genz_to_english
app = Flask(__name__)

@app.route('/api/translate', methods=['POST'])
def translate():
    body = request.get_json()
    print("Entering translate function")
    sentence = body["sentence"]
    translation = translate_genz_to_english(sentence)    
    
    response = { "translation": translation }
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5328)