# import pandas as pd
import numpy as np
from flask import Flask,render_template,request
import pickle
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer,WordNetLemmatizer
import re
def clean_text_data(data):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    wn = WordNetLemmatizer()
    data = data.lower()
    #Remove special characters
    data = re.sub(r'[^0-9a-zA-Z]', ' ', data)
    #Remove extra spaces
    data = re.sub(r'\s+', ' ', data)
    #Remove stopwords
    data = " ".join(w for w in data.split() if w not in stop_words)
    #stemming the words
    #Perform Lemmatization then Stemming
    words = data.split()
    l = []
    for w in words:
        w = re.sub('ly$','',w)
        w = wn.lemmatize(w,pos='v')
        w = wn.lemmatize(w,pos='n')
        w = wn.lemmatize(w,pos='a')
        w = ps.stem(w)
        l.append(w)
    data = " ".join(w for w in l)
    #data = l
    return data

def text_cleaner(text):
    return [clean_text_data(text)]

app = Flask(__name__)
@app.route('/')

def home():
    return render_template('home.html')
@app.route('/',methods=['GET','POST'])
def predict():
    if request.method =="POST":
        file_name = 'svm.p'
        with open(file_name,'rb') as pickled:
             data = pickle.load(pickled)
             model= data['model']
             print('model loaded')
        X = [x for x in request.form.values()]
        X = X[0]
        print(model) 
        print(X)
        Y = int(model.predict(X))
        print('Prediction {} : '.format(Y))
        if Y==0:
            pred = 'HAM :)'
        else:
            pred = 'SPAM *|*'
        print(pred)
    return render_template('home.html',prediction=pred)
if __name__=='__main__':
    app.run()