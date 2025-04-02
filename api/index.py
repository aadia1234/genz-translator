from flask import Flask, request
from translate import translate_sentence
import os
app = Flask(__name__)

@app.route('/api/translate', methods=['POST'])
def translate():
    sentence = request.get_data().decode("utf-8")
    print("Entering translate function")
    translation = translate_sentence(sentence)    
    return translation

if __name__ == '__main__':
    app.run(port=5328)