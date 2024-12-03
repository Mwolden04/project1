#import pytest
from bs4 import BeautifulSoup
import requests
import re
import ollama
import numpy as np 
import matplotlib.pyplot as plt 
from abc import ABC, abstractmethod

class DataHold(ABC):    #sets up abstract class for gaining either comments or reviews
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_string(self, string):
        pass
    
    def check_array(self):                  #I used this to simply check that everything accurately functioned
        for i in range(self.iteration):     
            print(self.Keep[i])


class CommentLibrar(DataHold):                        #I used this to keep track of the comments. It only keeps track of iself.
    def __init__(self):
        self.iteration = 0
        self.Keep = []

    def add_string(self, string):
        self.Keep.append(string)
        self.iteration = self.iteration + 1


class Sentiments(DataHold):                        #This is to check for the strings if it is positive, neutral or negative

    def __init__(self): #will keep track of different reviews, not just how many reviews are in it
        self.iteration = 0
        self.Keep = []
        self.neutral = 0
        self.positive = 0
        self.negative = 0


    def add_string(self, string):   # checks only the first 7 letters of a response to see what to classify as a comment
        if(string == "Positiv"):
            string = string + "e"
            self.positive = self.positive + 1
        elif(string == "Negativ"):
            string = string + "e"
            self.negative = self.negative + 1
        else:
            string = "Neutral"     
            self.neutral = self.neutral + 1   
        self.Keep.append(string)
        self.iteration = self.iteration + 1

def graph_of_five_things(product1, product2, product3, product4, product5): #This function creates a graph out of 5 objects of my Sentiments class
    # set width of bar 
    barWidth = 0.25
    fig = plt.subplots(figsize =(9, 8)) 

    # set height of bar 
    positive_rev = [product1.positive, product2.positive, product3.positive, product4.positive, product5.positive] 
    neutral_rev = [product1.neutral, product2.neutral, product3.neutral, product4.neutral, product5.neutral] 
    negative_rev = [product1.negative, product2.negative, product3.negative, product4.negative, product5.negative] 

    # Set position of bar on X axis 
    br1 = np.arange(len(positive_rev)) 
    br2 = [x + barWidth for x in br1] 
    br3 = [x + barWidth for x in br2] 

    plt.bar(br1, positive_rev, color ='b', width = barWidth, 
            edgecolor ='grey', label ='positive') 
    plt.bar(br2, neutral_rev, color ='g', width = barWidth, 
            edgecolor ='grey', label ='neutral') 
    plt.bar(br3, negative_rev, color ='r', width = barWidth, 
            edgecolor ='grey', label ='negative') 

    # Adding Xticks 
    plt.xlabel('Product', fontweight ='bold', fontsize = 15) 
    plt.ylabel('Reviews', fontweight ='bold', fontsize = 15) 
    plt.xticks([r + barWidth for r in range(len(positive_rev))], 
            ['Nintendo Switch', 'Switch Light', 'Switch OLED', 'Play Station 4', 'Null product'])

    plt.legend()
    plt.show()

def remove_emojis(data): #This function was used when writing to files to remove emojis from the text as txt files can't handle emojis
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)

prod1 = Sentiments()
prod2 = Sentiments() 
prod3 = Sentiments() 
prod4 = Sentiments() 
prod5 = Sentiments()



def test_answer():  #checks to see if a graph outputs and makes sure that there are 15 different "bars" that would exist if I had set numbers in
    numberGame = 0
    graph_of_five_things(prod1, prod2, prod3, prod4, prod5)
    if(prod1.negative == 0 and prod1.positive == 0 and prod1.neutral == 0):
        numberGame = numberGame + 1
    if(prod2.negative == 0 and prod2.positive == 0 and prod2.neutral == 0):
        numberGame = numberGame + 1
    if(prod3.negative == 0 and prod3.positive == 0 and prod3.neutral == 0):
        numberGame = numberGame + 1
    if(prod4.negative == 0 and prod4.positive == 0 and prod4.neutral == 0):
        numberGame = numberGame + 1
    if(prod5.negative == 0 and prod5.positive == 0 and prod5.neutral == 0):
        numberGame = numberGame + 1
    assert numberGame == 5

def test_answer2(): #makes sure that add string for Sentiments counts how many positives there are
    for i in range(3):
        prod1.add_string("Positiv")
    assert prod1.positive == 3

def test_answer5(): #makes sure that add string for negative counts how many negatives there are
    for i in range(3):
        prod1.add_string("Negativ")
    assert prod1.negative == 3

def test_answer6(): #makes sure that add string for Neutral counts how many neutral there are
    for i in range(3):
        prod1.add_string("Neutral")
    assert prod1.neutral == 3

def test_answer3(): #makes sure that the commentlib class actually gets strings
    lib = CommentLibrar()
    
    lib.add_string('why')
    assert lib.Keep == ['why']

def test_answer4(): #ensures that remove emojis will remove any emojis that it finds.
    emoted_word = "\U0001F600yay"
    assert remove_emojis(emoted_word) == "yay"


