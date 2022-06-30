from flask import Flask, request, url_for, redirect, render_template, jsonify
import pandas as pd
import pickle
import numpy as np
import porter
# Initalise the Flask app
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
vec = pickle.load(open('vec.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    features = [x for x in request.form.values()]
    print(features)
    email = features[1]
    email_clean = porter.processEmail(email)
    email_trans = vec.transform([email_clean])
    spam = model.predict(email_trans)
    print(spam)
    if spam[0]==0:
        return render_template('index.html', pred="This is not spam and seems to be pretty legit.")
    else:
        return render_template('index.html', pred="This is probably spam. Although the model is a bit too strict on what qualifies as not spam.")
        
        


if __name__ == '__main__':
    app.run(debug=True)
