import praw as praw

from textblob import TextBlob

from datetime import datetime

from time import time

import json

import pandas

from emoji import UNICODE_EMOJI

from nltk import WordNetLemmatizer

from nltk import FreqDist

import nltk

nltk.download('punkt')

nltk.download('wordnet')

#import gensim

#gensim_stopwords = gensim.parsing.preprocessing.STOPWORDS

#from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

stopwords = {'aint', 'years', 'thread', 'year', 'one', 'contact', 'comment', 'first', 'last', 'bot', 'remove',
             'removed', 'vote', 'violating', 'flair', 'shitposts', 'shitpost', 'say', 'answer', 'related', 'posting',
             'people', 'group', 'first', 'link', 'retarded', 'weekend', 'edit', 'like', '\'m', 'also', '\'re', '\\"',
             '\,', 'n\'t', '\'s', 'discussion', 'know', 'get', 'fuck', 'go', 'question', 'report', 'ban', 'violations',
             'click', 'post', 'https', 'http', 'their', ',', '.', '/', 'subreddit', 'see', 'rule', 'please', 'as', 'in',
             'i', 'they', 'then', 'not', 'ma', 'here', 'other', 'won', 'up', 'weren', 'being', 'we', 'those', 'an',
             'them', 'which', 'him', 'so', 'yourselves', 'what', 'own', 'has', 'should', 'above', 'in', 'myself',
             'against', 'that', 'before', 't', 'just', 'into', 'about', 'most', 'd', 'where', 'our', 'or', 'such',
             'ours', 'of', 'doesn', 'further', 'needn', 'now', 'some', 'too', 'hasn', 'more', 'the', 'yours', 'her',
             'below', 'same', 'how', 'very', 'is', 'did', 'you', 'his', 'when', 'few', 'does', 'down', 'yourself', 'i',
             'do', 'both', 'shan', 'have', 'itself', 'shouldn', 'through', 'themselves', 'o', 'didn', 've', 'm', 'off',
             'out', 'but', 'and', 'doing', 'any', 'nor', 'over', 'had', 'because', 'himself', 'theirs', 'me', 'by',
             'she', 'whom', 'hers', 're', 'hadn', 'who', 'he', 'my', 'if', 'will', 'are', 'why', 'from', 'am', 'with',
             'been', 'its', 'ourselves', 'ain', 'couldn', 'a', 'aren', 'under', 'll', 'on', 'y', 'can', 'they', 'than',
             'after', 'wouldn', 'each', 'once', 'mightn', 'for', 'this', 'these', 's', 'only', 'haven', 'having', 'all',
             'don', 'it', 'there', 'until', 'again', 'to', 'while', 'be', 'no', 'during', 'herself', 'as', 'mustn',
             'between', 'was', 'at', 'your', 'were', 'isn', 'wasn'}

# -------------------------------------------------------------------------------#

#definition for running scraper
def scrapedata(subredditname,wordname,postcount,commentcount,replycount,flairfilter):

    # starting time

    start = time()

    lem = WordNetLemmatizer()

    # Inputs:-----------------------------------------------------------------------#

    I_subreddit = subredditname

    I_postcount = int(postcount)

    I_comment_count = int(commentcount)

    I_reply_count = int(replycount)

    I_wordtocount = wordname

    I_flairfilter = [flairfilter]

    # Outputs:-----------------------------------------------------------------------#

    I_date = []

    I_frequency = []

    I_score = []

    I_type = []

    I_allwords = []

    I_allnumbers = []

    I_allfliars = []

    I_sentiment = []

    # Definitions------------------------------------------------------------------#

    # defenition for checking polarity
    def getpolarity(text):

        blob = TextBlob(text)

        sentiment = blob.sentiment
        # calculates overall sentiment
        I_sentiment.append((sentiment[1]+sentiment[0])/2)

    # -----------------------------------------------------------------------------#

    # defenition for checking word occurence and cleaning words.
    def getwordcount(text):

        blob = TextBlob(text)

        frequency = str(blob).count(I_wordtocount)

        for words in blob.words:

            lowerwords = words.lower()

            # print("Original - " + lowerwords)

            if (len(lowerwords) >= 3) and (len(lowerwords) <= 9):

                for character in lowerwords:

                    if character not in UNICODE_EMOJI:

                        if any(character.isdigit() for character in lowerwords):
                            I_allnumbers.append(lowerwords)
                            break

                        lemmedwords = lem.lemmatize(lowerwords, "v")

                        lowerlemmedwords = lemmedwords.lower()

                        # print("lemmed - " + lowerlemmedwords)

                        #if (lowerlemmedwords not in stopwords) and (lowerlemmedwords not in gensim_stopwords) and (
                                    #lowerlemmedwords not in ENGLISH_STOP_WORDS):

                        if (lowerlemmedwords not in stopwords):

                            if (len(lowerlemmedwords) >= 3):

                                I_allwords.append(lowerlemmedwords)

        return frequency


    # -----------------------------------------------------------------------------#
    # mean
    def Average(lst):

        return sum(lst) / len(lst)

    # -----------------------------------------------------------------------------#
    # roundup
    def roundupnew (list):

        newdata = []

        for x in list:

            newdata.append(round(x, 2))

        return newdata

    # -----------------------------------------------------------------------------#
    # get word frequnecy
    def createpaireddict(fdistwordlist):

        localfinal = []

        numberofelements = 30

        fdist = FreqDist(fdistwordlist)

        slicedfdist = dict(fdist.most_common(numberofelements))

        for keys, values in slicedfdist.items():

            valxy = ['x', 'y']

            splitlist = [keys, values]

            res = dict(zip(valxy, splitlist))

            localfinal.append(res)

        return localfinal

    # -----------------------------------------------------------------------------#

    # create a reddit object with details - to use json!!
    reddit = praw.Reddit(client_id='YtDeMC6y6k2TlA',
                         client_secret='9TyGlxTutmCUqS_v53A2BlHyTszJSg',
                         password='vensionbob@112',
                         user_agent='testapp',
                         username='Fun_Mixture_7200')

    # Create a subreddit Object
    subreddit = reddit.subreddit(I_subreddit)

    # Sorting Posts by hot and setting Limits
    newposts = subreddit.hot(limit=I_postcount)

    # ------------------------------------------------------------------------------#

    I_postcount = 0

    I_commentcount = 0

    I_replycount = 0

    # ------------------------------------------------------------------------------#

    # iterating throught posts
    for posts in newposts:

        if (posts.link_flair_text not in I_flairfilter):

            print(posts.link_flair_text)

            # adds post flair to list
            I_allfliars.append(str(posts.link_flair_text))

            I_postcount = I_postcount + 1

            print("Reading Post No. " + str(I_postcount))

            # avoids the 'More_Comment' Error
            posts.comments.replace_more(limit=0)

            # --------------------------------------------------------------#

            # append type
            I_type.append("P")

            # append post upvotes
            I_score.append(posts.score)

            # append post date
            I_date.append(datetime.fromtimestamp(posts.created))

            # append word frequency
            I_frequency.append(getwordcount(str(posts.title)))

            # append sentiment
            getpolarity(str(posts.title))

            # --------------------------------------------------------------#

            # print("$POST$ " + posts.title + "\n" )

            for comments in posts.comments[:I_comment_count]:

                I_commentcount = I_commentcount + 1

                print("Reading Comment No. " + str(I_commentcount))

                # --------------------------------------------------------------#

                # append type
                I_type.append("C")

                # append post upvotes
                I_score.append(comments.score)

                # append comment date
                I_date.append(datetime.fromtimestamp(comments.created))

                # append word frequency
                I_frequency.append(getwordcount(str(comments.body)))

                # append sentiment
                getpolarity(str(comments.body))

                # --------------------------------------------------------------#

                # print("  $COMMENT$ " + comments.body + "\n")

                if len(comments.replies) > 0:

                    for reply in comments.replies[:I_reply_count]:
                        I_replycount = I_replycount + 1

                        print("Reading Reply No.. " + str(I_replycount))

                        # --------------------------------------------------------------#

                        # append type
                        I_type.append("R")

                        # append post upvotes
                        I_score.append(reply.score)

                        # append reply date
                        I_date.append(datetime.fromtimestamp(reply.created))

                        # append word frequency
                        I_frequency.append(getwordcount(str(reply.body)))

                        # append sentiment
                        getpolarity(str(reply.body))


    # --------------------------------------------------------------#
    # grouped data for hourly plots
    I_hourlydate = []

    for date in I_date:

        year = str(date.year)

        month = "0" + str(date.month)

        day = "0" + str(date.day)

        hour = "0" + str(date.hour)

        #newdate = ((year[2:]) + '.' + str(month[-2:]) + '.' + day[-2:] + ' (' + hour[-2:] + ":00)")

        newdate = (day[-2:] + '.' + str(month[-2:]) + '.' + year[2:] + '-'+hour[-2:]+ "H")

        I_hourlydate.append(str(newdate))

    Grouped_hourlydate = []

    for x in I_hourlydate:

        if x not in Grouped_hourlydate:

            Grouped_hourlydate.append(x)

    Grouped_hourlydate = sorted(Grouped_hourlydate)

    # Grouped data output
    # ----------------------------------------------------------------------------------------------#
    # 1) Grouped data with Frequency

    frequencygroup = {'Dates': I_hourlydate, 'Frequency': I_frequency}

    frequencytable = pandas.DataFrame(frequencygroup)

    frequencytable = frequencytable.groupby('Dates').sum()

    # ----------------------------------------------------------------------------------------------#
    # 2) Grouped data with Sent Polarity

    Sentimentgroup = {'Dates': I_hourlydate, 'Sentiment': I_sentiment}

    Sentimenttable = pandas.DataFrame(Sentimentgroup)

    Sentimenttable = Sentimenttable.groupby('Dates').mean()

    # ----------------------------------------------------------------------------------------------#
    # 3) Grouped data with Score

    Scoregroup = {'Dates': I_hourlydate, 'Score': I_score}

    Scoretable = pandas.DataFrame(Scoregroup)

    Scoretable = Scoretable.groupby('Dates').sum()

    # -------------------------------------------------------------------------------#
    #Outputs:

    #type_frequency = I_type

    allflair_frequency = (createpaireddict(I_allfliars))

    allnumber_frequency = (createpaireddict(I_allnumbers))

    allwords_frequency = (createpaireddict(I_allwords))

    word_frequency = frequencytable['Frequency'].tolist()

    score_frequency = Scoretable['Score'].tolist()

    sentiment_frequency = roundupnew(Sentimenttable['Sentiment'].tolist())

    # end time
    end = time()
    # --------------------------------------------------------------------------------#
    print("Total Posts,Comments & Replies = " + str(len(I_date)) + "\n")

    print("Time taken to run =" + str(end - start) + "\n")

    # ---------------------------------------------------------------------------------------#
    #test area:

    #print(createpaireddict(I_allwords))

    # ---------------------------------------------------------------------------------------#

    return json.dumps(word_frequency),json.dumps(Grouped_hourlydate),json.dumps(sentiment_frequency),json.dumps(score_frequency),json.dumps(allwords_frequency),json.dumps(allnumber_frequency),json.dumps(allflair_frequency)

# ---------------------------------------------------------------------------------------#
# test area:

#word_time_frequency_data = scrapedata("wallstreetbets","trump",2,100,100,"meme")

# ---------------------------------------------------------------------------------------#
