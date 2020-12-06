pip install praw textblob nltk seaborn emoji gensim sklearn

import nltk
nltk.download('punkt')
from nltk import *
nltk.download('wordnet')

from gensim.parsing.preprocessing import remove_stopwords
import gensim

gensim_stopwords = gensim.parsing.preprocessing.STOPWORDS

from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

stopwords = {'aint','years','thread','year','one','contact','comment','first','last','bot','remove','removed','vote','violating','flair','shitposts','shitpost','say','answer','related','posting','people','group','first','link','retarded','weekend','edit','like','\'m','also','\'re','\\"','\,','n\'t','\'s','discussion','know','get','fuck','go','question','report','ban','violations','click','post','https','http','their',',','.','/','subreddit','see','rule','please','as','in','i','they', 'then', 'not', 'ma', 'here', 'other', 'won', 'up', 'weren', 'being', 'we', 'those', 'an', 'them', 'which', 'him', 'so', 'yourselves', 'what', 'own', 'has', 'should', 'above', 'in', 'myself', 'against', 'that', 'before', 't', 'just', 'into', 'about', 'most', 'd', 'where', 'our', 'or', 'such', 'ours', 'of', 'doesn', 'further', 'needn', 'now', 'some', 'too', 'hasn', 'more', 'the', 'yours', 'her', 'below', 'same', 'how', 'very', 'is', 'did', 'you', 'his', 'when', 'few', 'does', 'down', 'yourself', 'i', 'do', 'both', 'shan', 'have', 'itself', 'shouldn', 'through', 'themselves', 'o', 'didn', 've', 'm', 'off', 'out', 'but', 'and', 'doing', 'any', 'nor', 'over', 'had', 'because', 'himself', 'theirs', 'me', 'by', 'she', 'whom', 'hers', 're', 'hadn', 'who', 'he', 'my', 'if', 'will', 'are', 'why', 'from', 'am', 'with', 'been', 'its', 'ourselves', 'ain', 'couldn', 'a', 'aren', 'under', 'll', 'on', 'y', 'can', 'they', 'than', 'after', 'wouldn', 'each', 'once', 'mightn', 'for', 'this', 'these', 's', 'only', 'haven', 'having', 'all', 'don', 'it', 'there', 'until', 'again', 'to', 'while', 'be', 'no', 'during', 'herself', 'as', 'mustn', 'between', 'was', 'at', 'your', 'were', 'isn', 'wasn'}

import praw as praw

from textblob import TextBlob

import datetime

import pandas

import time

from emoji import UNICODE_EMOJI

#-------------------------------------------------------------------------------#

# starting time
start = time.time()

lem = WordNetLemmatizer()

porter = PorterStemmer()
#Inputs:-----------------------------------------------------------------------#

I_subreddit = 'wallstreetbets'

I_postcount = 5

I_comment_count = 2

I_reply_count = 2

I_wordtocount = 'tsla'

#Outputs:-----------------------------------------------------------------------#

I_date = []

I_frequency = []

I_score = []

I_type = []

I_sentsubjectivity = []

I_sentpolarity = []

I_allwords = []

#Definitions------------------------------------------------------------------#

# defenition for checking polarity
def getpolarity(text):
    
    blob = TextBlob(text)
    
    sentiment = blob.sentiment
    
    I_sentsubjectivity.append(sentiment[1])
    
    I_sentpolarity.append(sentiment[0])

#-----------------------------------------------------------------------------#

# defenition for checking word occurence and cleaning words.
def getwordcount(text):
    
    blob = TextBlob(text)
    
    frequency = str(blob).count(I_wordtocount)
    
    for words in blob.words:
        
        lowerwords = words.lower()
        
        print("Original - " + lowerwords)
        
        if (len(lowerwords) >= 3) and (len(lowerwords) <= 9):
                
            for character in lowerwords:
                    
                if character not in UNICODE_EMOJI:
                        
                    if any (character.isdigit() for character in lowerwords):
                            
                        break
                        
                    lemmedwords = lem.lemmatize(lowerwords,"v")
                    
                    lowerlemmedwords=lemmedwords.lower()
                    
                    print("lemmed - " + lowerlemmedwords)
                    
                    if (lowerlemmedwords not in stopwords) and (lowerlemmedwords not in gensim_stopwords) and(lowerlemmedwords not in ENGLISH_STOP_WORDS):
                        
                        portedwords = porter.stem(lowerlemmedwords)
                        
                        print("ported - " + lowerlemmedwords)
                        
                        if (len(lowerlemmedwords) >= 3):
                            
                            I_allwords.append(lowerlemmedwords)
                            
                            
    return frequency

#-----------------------------------------------------------------------------#
#mean
def Average(lst):
    
    return sum(lst) / len(lst) 

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
    
    #append type
    I_type.append("P")
    
    #append post upvotes
    I_score.append(posts.score)
    
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
        
        #append type
        I_type.append("C")
        
        #append post upvotes
        I_score.append(comments.score)
    
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
                
                #append type
                I_type.append("R")
                
                #append post upvotes
                I_score.append(reply.score)
        
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
import seaborn

import matplotlib

from matplotlib import pyplot as plot

from matplotlib import rcParams

#--------------------------------------------------------------#

# figure size in inches
rcParams['figure.figsize'] = 25,15

print("Total Posts,Comments & Replies = " + str(len(I_date)) + "\n")
    
print("There are - " + str(sum(I_frequency))  + " mentions of " + "| " + I_wordtocount + " |" + "\n")

print("Time taken to run =" + str(end - start) + "\n")

#--------------------------------------------------------------#

#Average polarity calculations(Overall)
try:
    
    actualvaluespol = (len(I_sentpolarity) - (I_sentpolarity.count(0)))

    sumpolarity = sum(I_sentpolarity)

    avgpolarity = sumpolarity/actualvaluespol

    print('Average polarity = ' + str(avgpolarity) + "\n")

    #Average subjectivity calculations(Overall)

    actualvaluessub = (len(I_sentsubjectivity) - (I_sentsubjectivity.count(0)))

    sumsubjectivity = sum(I_sentsubjectivity)

    avgsubjectivty = sumsubjectivity/actualvaluessub

    print('Average Subjectivity = ' + str(avgsubjectivty))
    
except:
    
    pass
#--------------------------------------------------------------#
# all data
data = {'Dates' : I_date, 'Frequency': I_frequency, 'Sentiment_Polarity': I_sentpolarity, 'SentSubjectivity': I_sentsubjectivity,'Score': I_score,'Type': I_type}
    
table = pandas.DataFrame(data)

with pandas.option_context('display.max_rows', 3, 'display.max_columns', None):
    
    display(table)
    
#----------------------------------------------------------------------------------------------#
# grouped data
I_hourlydate = []

for date in I_date:
    
    year = str(date.year)
    
    month =  "0" +str(date.month)
    
    day =  "0" +str(date.day)
    
    hour =  "0" +str(date.hour)
    
    newdate = ((year[2:]) + '-' + str(month[-2:]) + '-' +  day[-2:] + ' (' +  hour[-2:]+":00)")
    
    I_hourlydate.append(str(newdate))
    
#----------------------------------------------------------------------------------------------#    
#1) Grouped data with Frequency

frequencygroup = {'Dates' : I_hourlydate, 'Frequency': I_frequency}

frequencytable = pandas.DataFrame(frequencygroup)

frequencytable = frequencytable.groupby('Dates').sum()

#----------------------------------------------------------------------------------------------#
#2) Grouped data with Sent Polarity

Polaritygroup = {'Dates' : I_hourlydate, 'Sentiment_Polarity': I_sentpolarity}

Polaritytable = pandas.DataFrame(Polaritygroup)

Polaritytable = Polaritytable.groupby('Dates').mean()

#----------------------------------------------------------------------------------------------#
#3) Grouped data with Sent Polarity

Subjectivitygroup = {'Dates' : I_hourlydate, 'SentSubjectivity': I_sentsubjectivity}

Subjectivitytable = pandas.DataFrame(Subjectivitygroup)

Subjectivitytable = Subjectivitytable.groupby('Dates').mean()

#----------------------------------------------------------------------------------------------#
#4) Grouped data with Score

Scoregroup = {'Dates' : I_hourlydate, 'Score': I_score}

Scoretable = pandas.DataFrame(Scoregroup)

Scoretable = Scoretable.groupby('Dates').sum()

#----------------------------------------------------------------------------------------------# 
#print all tables
with pandas.option_context('display.max_rows', 1, 'display.max_columns', None):
    
    display(frequencytable,Polaritytable,Subjectivitytable,Scoretable)
    
#----------------------------------------------------------------------------------------------#  
#plot all graphs

seaborn.set(style="white")  

seaborn.despine(offset=10, trim=True)

seaborn.set_context("poster", font_scale = 1, rc={"grid.linewidth": 5})

fig, axs = plot.subplots(nrows=4,figsize=(35,25))

plot1 = seaborn.lineplot(data=frequencytable, x="Dates", y="Frequency",ax=axs[0])

plot.draw()

plot1.set_xticklabels(plot1.get_xticklabels(), rotation=90)

plot2 = seaborn.lineplot(data=Scoretable, x="Dates", y="Score",ax=axs[1])

plot.draw()

plot2.set_xticklabels(plot1.get_xticklabels(), rotation=90)

plot3 = seaborn.lineplot(data=Polaritytable, x="Dates", y="Sentiment_Polarity",ax=axs[2])

plot.draw()

plot3.set_xticklabels(plot1.get_xticklabels(), rotation=90)

plot4 = seaborn.lineplot(data=Subjectivitytable, x="Dates", y="SentSubjectivity",ax=axs[3])

plot.draw()

plot4.set_xticklabels(plot1.get_xticklabels(), rotation=90)

fig.tight_layout()


#---------------------------------------------------------------------------------------#

import matplotlib

from matplotlib import pyplot as plot

import seaborn

from matplotlib import rcParams

# figure size in inches
rcParams['figure.figsize'] = 25,25

cleaned_words = []

frequentwords = []

frequentwordscount = []

#-------------------------------------------------------------------------------#

fdist = FreqDist(I_allwords)

#-------------------------------------------------------------------------------#

sorted_dict = {}

sorted_keys = sorted(fdist, key=fdist.get)

for w in sorted_keys:
    
    sorted_dict[w] = fdist[w]
    
dictwords = dict(reversed(list(sorted_dict.items())))    
#-------------------------------------------------------------------------------#

for keys,values in dictwords.items():
    
    frequentwords.append(keys)
    
    frequentwordscount.append(values)
    
    #print(keys,values)
    
 #-------------------------------------------------------------------------------#   

frequencydata = { 'Frequency': frequentwordscount[:100], 'Words' : frequentwords[:100]}

freqtable = pandas.DataFrame(frequencydata)

with pandas.option_context('display.max_rows', 5, 'display.max_columns', None):
    
    display(freqtable)

fdist.plot(50,cumulative=False)

bargraph.set_xticklabels(bargraph.get_xticklabels(), rotation=90)

bargraph = seaborn.barplot(x='Frequency', y='Words', data=freqtable, edgecolor="1")

plot.show()
