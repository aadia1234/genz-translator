from transformers import pipeline, AutoTokenizer,AutoModelForSeq2SeqLM, Seq2SeqTrainingArguments, Seq2SeqTrainer, DataCollatorForSeq2Seq
from datasets import Dataset
import pandas as pd
import numpy as np
import evaluate

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