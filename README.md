# Project 1: SMS Spam Detector - Overview
Spam is an advertising material send by email or SMS to people who have not asked for. In this project, we will build an SMS Spam Detector with Machine Learning algorithms. It is built with the “spam.csv” dataset downloaded from Kaggle. The class is highly imbalanced so the metric chosen for this project are the Precision, Recall, and F1 score.
The projects have the following steps:
* Clean the message text data by removing noises 
* Build a pipeline to preprocess the clean text data and select the relevant features for model building;
* Build Machine Learning models and tune hyperparamters with GridsearchCV;
* Build a simple web app with Flask;
Requirements:
* Python 3.8
* Numpy
* Pandas
* Scikit-Learn
* Flask
### Step 1: Text Cleaning:
Removing the noises such as punctuations, numbers, special characters, stopwords, lemmatization and stemming reduce its size and make it easier to transform into a feature vectors before feeding them into a classifier. The function “clean_text_data” perform this task on the imported Pandas Dataframe.
### Step 2: Text preprocessing and feature selection:
The clean text is then transformed into a feature vectors with the HashingVectorizer from Scikit-Learn. Then we will select the most relevant elements of the feature vectors by using a feature selector based on the coefficients of the Stochastic Gradient Descent Classifier model.
### Step 3: Model building:
With the function “train_models”, we will train the following models:
* Logistic Regression
* Decision Tree Classifier
* Support Vector Machine
* Random Forest Classifier
We picked Logistic Regression and the Support Vector Machine because they perform well, and didn’t overfit their training set. Then, we optimize the hyperparamters using GridSearchCV.
![spam_ml_pipeline](https://user-images.githubusercontent.com/105801284/204245907-cb75a519-6c12-4445-ab2b-1ca3af60741c.jpg)
### Build a Flask API endpoints:
The Flask API endpoints will be built so that we can make a request from that API to predict if a message is a “SPAM”. Our web app will take as input a message and return a predicted class.
