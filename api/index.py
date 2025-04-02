from flask import Flask, request
from flask_cors import CORS
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
app = Flask(__name__)

# Configure CORS properly - critical for Vercel deployment
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api/translate', methods=['POST'])
def translate():
    sentence = request.get_data().decode("utf-8")
    print("Entering translate function")
    # translation = translate_sentence(sentence)  
    translation = "WOW"
    return translation

@app.route('/api/translate', methods=['GET'])
def get_translation():  
    return "GET translation"

if __name__ == '__main__':
    # uvicorn("api.index:app", host="0.0.0.0", port=5328, reload=True)
    app.run(host='0.0.0.0', port=5328)
    
    
def translate_sentence(sentence):
    # Add the required prefix - THIS IS CRUCIAL
    prefix = "translate Shakespearean English to Modern English: "
    input_text = prefix + sentence
    
    model_path = "aadia1234/shakespeare-to-english"
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
    
    # Prepare the input
    inputs = tokenizer(input_text, return_tensors="pt")
    
    # Move inputs to the same device as the model
    device = model.device
    inputs = {k: v.to(device) for k, v in inputs.items()}
    
    # Generate translation with better parameters
    outputs = model.generate(inputs["input_ids"], max_new_tokens=40, do_sample=True, top_k=30, top_p=0.95)

    
    # Decode the output
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return translated_text