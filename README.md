# Introduction

This is a spam classifier with 97% accuracy. The classifier was trained on this dataset from [kaggle](https://www.kaggle.com/datasets/venky73/spam-mails-dataset).

There is also a small Flask app that is used for deploying the model on Heroku.

# Usage

If you simply want to find out an email is spam or not, you can go to [this site](https://spam-classifier-314.herokuapp.com/) and fill in the form details.

If you want to work with the model, the model and the vectorizer is stored in the repo with which you can transform the email contents and predict if it's spam locally by cloning this repo and loading the pickle files. 

The Flask app can also be run locally by running `python app.py` on your terminal.
