# SMS-spam-detetor
The aim of this project is to detect spam messages and classify them. We start from preprocessing the raw data until model building then we compared the performance of all the trained the classifier.

# Methods:
The dataset is a '.csv' file from www.kaggle.com. 
It has 5571 rows of samples and two columns representing the labels and the messages.
The data is imported by using Pandas library. 
We preprocess the text data with NLTK and Scikit-Learn (removing unecessary characters, stop words, stemming words,...).
 
The class was imbalanced so we oversample the minority class in the training set by using Synthetic Minority Oversampling TEchnique or SMOTE.
This technique will Increase minority class by introducing synthetic examples through connecting all k (default = 5) minority class nearest neighbors based on the Euclidian distance between the features spaces.

Then we train Machine Learning models : Logistic Regression, Decision Tree, Support Vector Machine, and Random Forest.

Logistic regression is a supervised machine learning model used to predict a binary outcome, such as yes or no, 
based on prior observations of a data set.
  ![sigmoid](https://user-images.githubusercontent.com/105801284/169696535-7bf8c498-965c-4e58-ae33-31d1105526d1.jpg)





It predicts a dependent data variable by analyzing the relationship between one or more existing independent variables. 
We fit our model to an S-shaped curve or the Sigmoid function that can take any real-value number between 0 and 1.
If the output of a certain input is beyond a defined threshold (let's say 0.5), the input is classified to the class 1 and to the class 0 otherwise.

Decision Tree classifer works like structure where internal  nodes represent a test on an attribute, each branch represents outcome of a test, and each leaf node represents class label, and the decision is made after computing all attributes.
  ![dtree](https://user-images.githubusercontent.com/105801284/169696573-10e85c8c-e080-48ec-b0cc-20ed0db5c2bc.jpg)


The key  objective of Support Vector Machine or SVM is to draw a optimal hyperplane that  better separates the two classes such that the margin is maximum between the hyperplane and the observations. 
  ![svm](https://user-images.githubusercontent.com/105801284/169696554-03709685-c3f8-4a99-833e-434dbc95ba5f.jpg)



Random forest is an ensemble methods or meta estimator that fits a number of decision tree classifiers on various sub-samples of the dataset and averages the predicted outcomes to improve the accuracy and control overfitting.
   ![rf](https://user-images.githubusercontent.com/105801284/169696564-6ab5f2f8-50e6-4006-9b2d-c68343722719.jpg)



In the end we sum up the scores of all the trained models.

# Required Library:
- NLTK
- Pandas
- Scikit-Learn
- imblearn

