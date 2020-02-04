from nltk.classify.util import apply_features
from nltk import NaiveBayesClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import os

from flask import current_app
import pickle, re
import collections


class SpamClassifier:

    def load_model(self, model_name):
        model_file = os.path.join(current_app.config['ML_MODEL_UPLOAD_FOLDER'], model_name+'.pk')
        model_word_features_file = os.path.join(current_app.config['ML_MODEL_UPLOAD_FOLDER'],model_name +'_word_features.pk')
        with open(model_file, 'rb') as mfp:
            self.classifier = pickle.load(mfp)
        with open(model_word_features_file, 'rb') as mwfp:
            self.word_features = pickle.load(mwfp)


    def extract_tokens(self, text, target):
        """returns array of tuples where each tuple is defined by (tokenized_text, label)
         parameters:
                text: array of texts
                target: array of target labels

        NOTE: consider only those words which have all alphabets and atleast 3 characters.
        """
        

    def get_features(self, corpus):
        """
        returns a Set of unique words in complete corpus.
        parameters:- corpus: tokenized corpus along with target labels

        Return Type is a set
        """
        

    def extract_features(self, document):
        """
        maps each input text into feature vector
        parameters:- document: string

        Return type : A dictionary with keys being the train data set word features.
                      The values correspond to True or False
        """
        

    def train(self, text, labels):
        """
        Returns trained model and set of unique words in training data
        """
        

    def predict(self, text):
        """
        Returns prediction labels of given input text.
        """
        


if __name__ == '__main__':

    print('Done')