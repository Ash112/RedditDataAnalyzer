pip install praw textblob nltk

import nltk
nltk.download('punkt')
from nltk import *
nltk.download('wordnet')

import praw as praw

from textblob import TextBlob

import datetime

import pandas

import time
#-------------------------------------------------------------------------------#
# starting time
start = time.time()

#Inputs:-----------------------------------------------------------------------#

I_subreddit = 'politics'

I_postcount = 4

I_comment_count = 3

I_reply_count = 3

I_wordtocount = 'Trump'

#Outputs:-----------------------------------------------------------------------#

#I_postcount = 0

I_date = []

I_frequency = []

I_sentsubjectivity = []

I_sentpolarity = []

I_allwords = []

#Definitions------------------------------------------------------------------#

# defenition for checking polarity
def getpolarity(text):
    
    blob = TextBlob(text)
    
    sentiment = blob.sentiment
    
    #for sentence in blob.sentences:
    I_sentsubjectivity.append(sentiment[1])
    
    I_sentpolarity.append(sentiment[0])
    
    #print("#POL# - [" + str(blob.sentiment) + "]" + "\n")

#-----------------------------------------------------------------------------#

# defenition for checking word occurence
def getwordcount(text):
    
    blob = TextBlob(text)
    
    frequency = str(blob).count(I_wordtocount)
    
    for word in blob.words:
        
        I_allwords.append(word)
    
    return frequency

#-----------------------------------------------------------------------------#

# create a reddit object with details - to use json!!
reddit = praw.Reddit(client_id='YtDeMC6y6k2TlA',
                     client_secret='9TyGlxTutmCUqS_v53A2BlHyTszJSg',
                     password='vensionbob@112',
                     user_agent='testapp',
                     username='Fun_Mixture_7200')

#Create a subreddit Object
subreddit = reddit.subreddit(I_subreddit)

# Sorting Posts by hot and setting Limits
newposts = subreddit.hot(limit=I_postcount)

#------------------------------------------------------------------------------#

I_postcount = 0

I_commentcount = 0

I_replycount = 0

#------------------------------------------------------------------------------#

# iterating throught posts    
for posts in newposts:
    
    I_postcount = I_postcount + 1
    
    print("Reading Post No. " + str(I_postcount))
    
    # avoids the 'More_Comment' Error
    posts.comments.replace_more(limit=0)
    
    # --------------------------------------------------------------#
    
    #append post date
    I_date.append(datetime.datetime.fromtimestamp(posts.created))
    
    #append word frequency
    I_frequency.append(getwordcount(str(posts.title)))
    
    #append sentiment
    getpolarity(str(posts.title))
    
    # --------------------------------------------------------------#

    #print("$POST$ " + posts.title + "\n" )
    
    for comments in posts.comments[:I_comment_count]:
        
        I_commentcount = I_commentcount + 1
    
        print("Reading Comment No. " + str(I_commentcount))
    
        # --------------------------------------------------------------#
    
        #append comment date
        I_date.append(datetime.datetime.fromtimestamp(comments.created))
    
        #append word frequency
        I_frequency.append(getwordcount(str(comments.body)))
    
        #append sentiment
        getpolarity(str(comments.body))
    
        # --------------------------------------------------------------#
        
        #print("  $COMMENT$ " + comments.body + "\n")
    
        if len(comments.replies)>0:
            
            for reply in comments.replies[:I_reply_count]:
                
                I_replycount = I_replycount + 1
    
                print("Reading Reply No.. " + str(I_replycount))
        
                # --------------------------------------------------------------#
    
                #append reply date
                I_date.append(datetime.datetime.fromtimestamp(reply.created))
    
                #append word frequency
                I_frequency.append(getwordcount(str(reply.body)))
    
                #append sentiment
                getpolarity(str(reply.body))
    
                # --------------------------------------------------------------#
                
                #print("   $REPLY$ " + reply.body + "\n")    
                
#end time                
end = time.time()

#--------------------------------------------------------------------------------#

def Average(lst):
    
    return sum(lst) / len(lst) 

print("Total Posts,Comments & Replies = " + str(len(I_date)) + "\n")
    
print("There are - " + str(sum(I_frequency))  + " mentions of " + "| " + I_wordtocount + " |" + "\n")

print("Time taken to run =" + str(end - start) + "\n")

print('Average polarity = ' + str(Average(I_sentpolarity)) + "\n")

print('Average Subjectivity = ' + str(Average(I_sentsubjectivity)))


data = {'Dates' : I_date, 'Frequency': I_frequency, 'Sentiment_Polarity': I_sentpolarity, 'SentSubjectivity': I_sentsubjectivity}
    
table = pandas.DataFrame(data)

with pandas.option_context('display.max_rows', 5, 'display.max_columns', None):
    
    display(table)


#---------------------------------------------------------------------------------------#
#visualizing frequency of words

import matplotlib

from matplotlib import pyplot as plot

cleaned_words = []

#custom stopwords list
stopwords = {'discussion','question','report','ban','violations','click','post','https','their',',','.','/','subreddit','see','rule','please','as','in','i','they', 'then', 'not', 'ma', 'here', 'other', 'won', 'up', 'weren', 'being', 'we', 'those', 'an', 'them', 'which', 'him', 'so', 'yourselves', 'what', 'own', 'has', 'should', 'above', 'in', 'myself', 'against', 'that', 'before', 't', 'just', 'into', 'about', 'most', 'd', 'where', 'our', 'or', 'such', 'ours', 'of', 'doesn', 'further', 'needn', 'now', 'some', 'too', 'hasn', 'more', 'the', 'yours', 'her', 'below', 'same', 'how', 'very', 'is', 'did', 'you', 'his', 'when', 'few', 'does', 'down', 'yourself', 'i', 'do', 'both', 'shan', 'have', 'itself', 'shouldn', 'through', 'themselves', 'o', 'didn', 've', 'm', 'off', 'out', 'but', 'and', 'doing', 'any', 'nor', 'over', 'had', 'because', 'himself', 'theirs', 'me', 'by', 'she', 'whom', 'hers', 're', 'hadn', 'who', 'he', 'my', 'if', 'will', 'are', 'why', 'from', 'am', 'with', 'been', 'its', 'ourselves', 'ain', 'couldn', 'a', 'aren', 'under', 'll', 'on', 'y', 'can', 'they', 'than', 'after', 'wouldn', 'each', 'once', 'mightn', 'for', 'this', 'these', 's', 'only', 'haven', 'having', 'all', 'don', 'it', 'there', 'until', 'again', 'to', 'while', 'be', 'no', 'during', 'herself', 'as', 'mustn', 'between', 'was', 'at', 'your', 'were', 'isn', 'wasn'}

#tokenized_word=word_tokenize(data)

#ps = PorterStemmer()

lem = WordNetLemmatizer()

for words in I_allwords:
    
    lowerwords = words.lower()
    
    if lowerwords not in stopwords:
        
        cleaned_words.append(lem.lemmatize(lowerwords,"v"))

# creating a frequency Dict
fdist = FreqDist(cleaned_words)

for keys,values in fdist.items():

    print(keys,values)

fdist.plot(25,cumulative=False)

plot.show()
