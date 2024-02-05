import streamlit as stt
import numpy as np
import PIL
PIL.Image.ANTIALIAS = PIL.Image.LANCZOS
import tflearn
import pickle
import nltk
from nltk.stem.lancaster import LancasterStemmer
import random
import json

@stt.cache_resource
def load():
    nltk.download('punkt')
    stemmer = LancasterStemmer()
    return stemmer

stemmer = load()

class Functions :


    def __init__(self) :
        with open("intents.json") as file:
            self.data = json.load(file)
        with open("data.pickle", "rb") as f:
            self.words, self.labels, self.training, self.output = pickle.load(f)
       
    def getData(self):
        return self.words, self.labels, self.training, self.output

    def getModel(self):

        net = tflearn.input_data(shape=[None, len(self.training[0])])
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, len(self.output[0]), activation="softmax")
        net = tflearn.regression(net)

        model = tflearn.DNN(net)
        model.load("model.tflearn")
        return model

    def bag_of_words(self, s, words):
        bag = [0 for _ in range(len(words))]
        s_words = nltk.word_tokenize(s)
        s_words = [stemmer.stem(word.lower()) for word in s_words]

        for se in s_words:
            for i, w in enumerate(words):
                if w == se:
                    bag[i] = 1
                
        return np.array(bag)

    def getResponse (self, model,labels,inp,words):

        results = model.predict([self.bag_of_words(inp,words)])
        results_index = np.argmax(results)

        tag = labels[results_index]

        for tg in self.data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']

        return random.choice(responses)
