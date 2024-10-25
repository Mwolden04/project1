from bs4 import BeautifulSoup
import requests
import re

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




inputF = open("url.txt", "r") #file containing URLs
outputF = open("comments 1.txt", "w") #file opens the comment 1.txt. It doesn't need to, it just helps me know that something can be put in if any error occurs

urls= inputF.readlines() #reads all URLs from txt file

product = 1 #important for knowing which product we are looking at.
commentCount = 0 #used to one) reset itself, 2) as something that will only happen once per product and 3) to count what comment im on in a product
comments = 0 #used to hold the number of comment per product
for url in urls:
    
    if(commentCount == 0): #When on a new product, depending on which comment im in, opens a text file to put comments in for one product and sets the amount of comments there are for a product
        match product:
        
            case 1:
            
                outputF = open("comments 1.txt", "w")
                comments = 15
            case 2:
            
                outputF = open("comments 2.txt", "w")
                comments = 171
            case 3:
            
                outputF = open("comments 3.txt", "w")
                comments = 72
            case 4:
            
                outputF = open("comments 4.txt", "w")
                comments = 47
    
        

    page = requests.get(url)  #gets the page

    soup = BeautifulSoup(page.text, 'html.parser') #goes through the HTML
    

    reviews = soup.find_all('div', class_= 'ebay-review-section') #finds everything with this class


    outputF.write(url + "\n\n\n") #writes what url is gotten in the comments page for safekeeping
    
    for review in reviews:  #for all reviews in a page, it writes each review to file
        texty = review.find('p', class_ = 'review-item-content rvw-wrap-spaces') #locks on to the html that has the text

        if(texty is not None): #checks if there is nothin in html
            texty = texty.get_text() #grabs text
            outputF.write(remove_emojis(str(texty))) #writes the text grabbed as string and removes emojis
            outputF.write("\n\n") #seperates comments for easier reading
        commentCount = commentCount +1 #one comment is added so it is ennumerated
        
    
    if(commentCount == comments):
        commentCount = 0 #resets comment count
        product = product + 1 #enumerates the product so that we can go onto the next product once enumerated.


inputF.close() #closes the files
outputF.close()