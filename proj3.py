from bs4 import BeautifulSoup
import requests
import re
import ollama
#from ollama import chat
from abc import ABC, abstractmethod
import numpy as np 
import matplotlib.pyplot as plt 

def ollama_ratings(library):    #gets phi-3 to generate a positive, negative, or neutral comment
    
    product = Sentiments()
    for i in range(library.iteration - 5):  #asks question. iteration has -5 due to some comments never even being able to output in first place
        response = ollama.generate(model='phi3', prompt = "Please tell me whether this" + 
                                   library.Keep[i] + 
                                   "is positive, negative or neutral in only one word.")
    
        word = str(response['response'])
        product.add_string(str(word[:7]))
        
    return product

def sentiments_to_txt(product, fname):  #This function takes one Sentiment class and a file name and puts all the reviews into a file
    file = open(fname, "w") #opens file
    for i in range(product.iteration):  #writes to file
        file.write(str(product.Keep[i]))
        file.write("\n")
    file.close()    #closes file

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




#start of code
library1 = CommentLibrar() #creates instances of libraries.
library2 = CommentLibrar()
library3 = CommentLibrar()
library4 = CommentLibrar()

inputF = open("url.txt", "r") #file containing URLs
outputF = open("comments1.txt", "w") #file opens the comment 1.txt. It doesn't need to, it just helps me know that something can be put in if any error occurs

urls= inputF.readlines() #reads all URLs from txt file

product = 1 #important for knowing which product we are looking at.
commentCount = 0 #used to one) reset itself, 2) as something that will only happen once per product and 3) to count what comment im on in a product
comments = 0 #used to hold the number of comment per product
for url in urls:
    
    if(commentCount == 0): #When on a new product, depending on which comment im in, opens a text file to put comments in for one product and sets the amount of comments there are for a product
        match product:
        
            case 1:
            
                outputF = open("comments1.txt", "w")
                comments = 15           #'Bug' that happens due to changes in Ebay
            case 2:
            
                outputF = open("comments2.txt", "w")
                comments = 95     #chnged from 171
            case 3:
            
                outputF = open("comments3.txt", "w")
                comments = 73
            case 4:
            
                outputF = open("comments4.txt", "w")
                comments = 47
    
        
    page = requests.get(url)  #gets the page
    soup = BeautifulSoup(page.text, 'html.parser') #goes through the HTML    
    reviews = soup.find_all('div', class_= 'ebay-review-section') #finds everything with this class 
    
    for review in reviews:  #for all reviews in a page, it writes each review to file
        texty = review.find('p', class_ = 'review-item-content rvw-wrap-spaces') #locks on to the html that has the text

        if(texty is not None): #checks if there is nothin in html
            texty = remove_emojis(str(texty.get_text())) #grabs text
            outputF.write(texty) #writes the text grabbed as string and removes emojis
            outputF.write("\n") #seperates comments for easier reading
            if(product == 1):
                library1.add_string(texty) #Depending on product value, adds comment to specific library
            elif(product == 2):
                library2.add_string(texty)
            elif(product == 3):
                library3.add_string(texty)
            elif(product == 4):
                library4.add_string(texty)

        commentCount = commentCount +1 #one comment is added so it is ennumerated
        print(commentCount)

        if commentCount == comments:    #added to stop reviews from going to the same txt file
            break
            
    if(commentCount == comments):
        commentCount = 0 #resets comment count
        product = product + 1 #enumerates the product so that we can go onto the next product once enumerated.


inputF.close() #closes the files
outputF.close()


#end project 2 part
#start project 1 part


product1 = Sentiments() #calls the sentiments that will be used
product2 = Sentiments()
product3 = Sentiments()
product4 = Sentiments()
product5 = Sentiments()

print("Getting Ollama's opinion for first product. This will take some time.")  #checks to see if comments are positive negative neutral.
product1 = ollama_ratings(library1)                                             #loads the ratings into each of the produts.
print("Getting Ollama's opinion for second product. This will take some time.")
product2 = ollama_ratings(library2)
print("Getting Ollama's opinion for third product. This will take some time.")
product3 = ollama_ratings(library3)
print("Getting Ollama's opinion for fourth product. This will take some time.")
product4 = ollama_ratings(library4)

print("Opinion obtained, now printing to sentiments text file") # outputs the sentiments to a text file
sentiments_to_txt(product1, "Senitments1.txt")
sentiments_to_txt(product2, "Sentiments2.txt")
sentiments_to_txt(product3, "Sentiments3.txt")
sentiments_to_txt(product4, "Sentiments4.txt")
sentiments_to_txt(product5, "Sentiments5.txt")
print("done printing")


#Beyond this point is where the main brunt of project 3 starts. It is the new parts

graph_of_five_things(product1, product2, product3, product4, product5)  #creates a graph of recieved items.