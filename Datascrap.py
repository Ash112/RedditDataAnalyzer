import praw as praw

from textblob import TextBlob

import datetime

import time

from emoji import UNICODE_EMOJI

from nltk import WordNetLemmatizer

#nltk.download('punkt')

#nltk.download('wordnet')

# -------------------------------------------------------------------------------#

stopwords = {'say', 'answer', 'related', 'posting', 'people', 'group', 'first', 'link', 'retarded', 'weekend', 'edit','like', '\'m', 'also', '\'re', '\\"', '\,', 'n\'t', '\'s', 'discussion', 'know', 'get', 'fuck', 'go','question', 'report', 'ban', 'violations', 'click', 'post', 'https', 'http', 'their', ',', '.', '/','subreddit', 'see', 'rule', 'please', 'as', 'in', 'i', 'they', 'then', 'not', 'ma', 'here', 'other', 'won','up', 'weren', 'being', 'we', 'those', 'an', 'them', 'which', 'him', 'so', 'yourselves', 'what', 'own','has', 'should', 'above', 'in', 'myself', 'against', 'that', 'before', 't', 'just', 'into', 'about','most', 'd', 'where', 'our', 'or', 'such', 'ours', 'of', 'doesn', 'further', 'needn', 'now', 'some', 'too','hasn', 'more', 'the', 'yours', 'her', 'below', 'same', 'how', 'very', 'is', 'did', 'you', 'his', 'when','few', 'does', 'down', 'yourself', 'i', 'do', 'both', 'shan', 'have', 'itself', 'shouldn', 'through','themselves', 'o', 'didn', 've', 'm', 'off', 'out', 'but', 'and', 'doing', 'any', 'nor', 'over', 'had','because', 'himself', 'theirs', 'me', 'by', 'she', 'whom', 'hers', 're', 'hadn', 'who', 'he', 'my', 'if','will', 'are', 'why', 'from', 'am', 'with', 'been', 'its', 'ourselves', 'ain', 'couldn', 'a', 'aren',
 'under', 'll', 'on', 'y', 'can', 'they', 'than', 'after', 'wouldn', 'each', 'once', 'mightn', 'for',
 'this', 'these', 's', 'only', 'haven', 'having', 'all', 'don', 'it', 'there', 'until', 'again', 'to',
 'while', 'be', 'no', 'during', 'herself', 'as', 'mustn', 'between', 'was', 'at', 'your', 'were', 'isn',
 'wasn'}


# -------------------------------------------------------------------------------#

# starting time
start = time.time()

lem = WordNetLemmatizer()

# Inputs:-----------------------------------------------------------------------#

I_subreddit = 'news'

I_postcount = 5

I_comment_count = 2

I_reply_count = 2

I_wordtocount = 'trump'

# Outputs:-----------------------------------------------------------------------#

I_date = []

I_frequency = []

I_score = []

I_type = []

I_sentsubjectivity = []

I_sentpolarity = []

I_allwords = []

# Definitions------------------------------------------------------------------#
# defenition for checking polarity
def getpolarity(text):
    blob = TextBlob(text)

    sentiment = blob.sentiment

    I_sentsubjectivity.append(sentiment[1])

    I_sentpolarity.append(sentiment[0])

# -----------------------------------------------------------------------------#
# defenition for checking word occurence and cleaning words.
def getwordcount(text):
    blob = TextBlob(text)

    frequency = str(blob).count(I_wordtocount)

    for words in blob.words:

        lowerwords = words.lower()

        #lemmedwords = lem.lemmatize(words, "n")

        if (len(lowerwords) >= 3) and (len(lowerwords) <= 9):

            for character in lowerwords:

                if character not in UNICODE_EMOJI:

                    if any(character.isdigit() for character in lowerwords):
                        break

                    lemmedwords = lem.lemmatize(lowerwords, "n")

                    if lemmedwords not in stopwords:

                        if (len(lowerwords) >= 3):

                            I_allwords.append(lemmedwords)

                            continue

    return frequency

# -----------------------------------------------------------------------------#
# mean
def Average(lst):
    return sum(lst) / len(lst)

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
    I_date.append(datetime.datetime.fromtimestamp(posts.created))

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
        I_date.append(datetime.datetime.fromtimestamp(comments.created))

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
                I_date.append(datetime.datetime.fromtimestamp(reply.created))

                # append word frequency
                I_frequency.append(getwordcount(str(reply.body)))

                # append sentiment
                getpolarity(str(reply.body))

                # --------------------------------------------------------------#

                # print("   $REPLY$ " + reply.body + "\n")

# end time
end = time.time()
# --------------------------------------------------------------------------------#
