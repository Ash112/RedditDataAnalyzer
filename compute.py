
from flask import Flask,request,render_template

# imports the python definition from file
from process import initialvalue

from datascraper import scrapedata

# creates a Flask application, named app
app = Flask(__name__)

# a route where we will intially render the main page with random values?
@app.route("/")
def hello():
    return render_template("index.html", word_frequency = initialvalue(),time_frequency =initialvalue(),sentiment_frequency = initialvalue())

# a route that takes user inpur(Subreddit and Word) returns frequency over time data
@app.route('/', methods =["GET", "POST"])
def userinput():

    subreddit = ""
    word = ""
    ffilter = ""
    postcount = ""
    commentcount = ""
    replycount = ""

    word_time_frequency_data = [initialvalue(),initialvalue(),initialvalue(),initialvalue()]

    if request.method == "POST":
        #inputs

        # getting input with subredditname in HTML form
        subreddit = request.form.get("sname")
        # getting input with word name HTML form
        word = request.form.get("wname")
        # getting input with flari filter HTML form
        ffilter = request.form.get("ffilter")
        # getting input with post count HTML form
        postcount = request.form.get("pcount")
        # getting input with comment count HTML form
        commentcount = request.form.get("ccount")
        # getting input with reply count HTML form
        replycount = request.form.get("rcount")

        if (subreddit == "") or (word == "") or (ffilter == "") or (postcount == "") or (commentcount == "") or (replycount == ""):

            print("no value ")

        else:
            #return processed output word frequency and timerange
            word_time_frequency_data = scrapedata(subreddit,word,postcount,commentcount,replycount,ffilter)

            #print(json.loads(word_time_frequency_data[1]))
            print(word_time_frequency_data[2])
            #print(word_time_frequency_data[1])
            #print(word_time_frequency_data[0])

    return render_template("index.html", word_frequency = word_time_frequency_data[0],time_frequency = word_time_frequency_data[1],sentiment_frequency = word_time_frequency_data[2],polarity_frequency = word_time_frequency_data[3])

# run the application
if __name__ == "__main__":

    # turn off debug when deploying
    app.run(debug=True)